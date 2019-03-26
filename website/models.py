from django.db import models

import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class Website(models.Model):
    website = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, default='')
    designation = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, default='Pakistan')
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    dribble =models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    aboutimg = models.ImageField(upload_to=get_image_path, blank=True, null=True)


    def __str__(self):
        return self.website