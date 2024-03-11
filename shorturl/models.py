from django.contrib.auth.models import User
from django.db import models
import random
import string


class SeoUrlModel(models.Model):
    to_url = models.URLField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    path = models.CharField(max_length=200, blank=True, unique=True)
    seo = models.ForeignKey('shorturl.SeoModel', on_delete=models.SET_NULL, blank=True, null=True)

    @staticmethod
    def generate_random_path(length=10):
        characters = string.ascii_letters + string.digits + "/"
        return ''.join(random.choice(characters) for _ in range(length))

    def has_seo(self):
        return self.seo is not None

    def save(self, *args, **kwargs):
        if self.path is None:
            self.path = self.generate_random_path()


class SeoModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

