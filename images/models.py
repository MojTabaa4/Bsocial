from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%M/%d')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(User, related_name='images_like', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
