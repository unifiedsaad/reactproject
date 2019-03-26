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
    dribble = models.CharField(max_length=100, blank=True, null=True)
    clients = models.IntegerField(max_length=50, blank=True, null=True)
    projects = models.IntegerField(max_length=50, blank=True, null=True)
    coffee = models.IntegerField(max_length=50, blank=True, null=True)
    design = models.TextField(help_text='Separate the servvices with comma')
    strategy = models.TextField(help_text='Separate the servvices with comma')
    code = models.TextField(help_text='Separate the servvices with comma')
    logo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    aboutimg = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    navbarimg = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.website


class portfolio(models.Model):
    website = models.ForeignKey(
        Website, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    website = models.ForeignKey(
        Website, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
