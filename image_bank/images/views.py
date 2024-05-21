from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import ImageForm
from .models import Image, Tag
import os
from uuid import uuid4
import requests


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

            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'images/upload.html', {'form': form})


def image_list(request):
    images = Image.objects.all()

    # Filtrage par nom original
    query = request.GET.get('q')
    if query:
        images = images.filter(original_name__icontains=query)

    for image in images:
        file_path = image.generated_name
        image_url = default_storage.url(file_path)
        image.image_url = image_url

    context = {'images': images}

    if not images:
        context['no_images'] = True

    return render(request, 'images/image_list.html', context)
