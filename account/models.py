from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%M/%d', blank=True)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_from_set')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    # following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
