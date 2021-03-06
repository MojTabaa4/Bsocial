from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('the given url not mach valid url extensions (jpg or jpeg)')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image_form = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image_form.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from url
        response = request.urlopen(url=image_url)
        image_form.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image_form.save()
        return image_form
