from django.contrib.auth.models import User
from django.db import models


class SeoUrlModel(models.Model):
    url = models.URLField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


# class CeoField
