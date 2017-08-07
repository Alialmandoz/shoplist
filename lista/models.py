from django.db import models

# Create your models here.


class Post(models.Model):
    texto = models.TextField(null=True, blank=True, )