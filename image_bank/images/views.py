from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from .forms import ImageForm
from .models import Image, Tag
import os
from uuid import uuid4
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            generated_name = f"{uuid4()}.{image_file.name.split('.')[-1]}"

            file_path = os.path.join(generated_name)
            default_storage.save(file_path, ContentFile(image_file.read()))

            image_instance = Image(
                image=file_path,
                original_name=image_file.name,
                generated_name=generated_name,
            )

            image_instance.save()

            image_url = image_instance.image.url

            subscription_key = os.getenv('COMPUTER_VISION_SUBSCRIPTION_KEY')
            endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')
            credentials = CognitiveServicesCredentials(subscription_key)
            computervision_client = ComputerVisionClient(endpoint, credentials)

            description, tags = describe_image(image_url, computervision_client)

            image_instance.description = description
            image_instance.save()
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                image_instance.tags.add(tag)

            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})


def describe_image(image_url, computervision_client):
    description = None
    tags = []
    try:
        description_result = computervision_client.describe_image(image_url)
        if description_result.captions:
            description = description_result.captions[0].text
        if description_result.tags:
            tags = description_result.tags
    except Exception as e:
        print(f"Error describing image: {e}")
    return description, tags


def image_list(request):
    images = Image.objects.all()

    query = request.GET.get('q')
    tag_id = request.GET.get('tag_id')

    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        images = images.filter(tags=tag)

    if query:
        images = images.filter(
            Q(original_name__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
        
    for image in images:
        file_path = image.generated_name
        image_url = default_storage.url(file_path)
        image.image_url = image_url

    context = {'images': images}

    if not images:
        context['no_images'] = True

    return render(request, 'images/image_list.html', context)


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'images/tag_list.html', {'tags': tags})


def delete_image(request, image_id):
    if request.method == 'POST':
        image = Image.objects.get(pk=image_id)
        default_storage.delete(image.image.name)
        image.delete()
    return HttpResponseRedirect(reverse('image_list'))
