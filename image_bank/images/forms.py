from django import forms
from .models import Image, Tag


class ImageForm(forms.ModelForm):
    # tags = forms.ModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

    class Meta:
        model = Image
        fields = ['image']
