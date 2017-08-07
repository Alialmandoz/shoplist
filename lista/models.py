from django.db import models

# Create your models here.


class Post(models.Model):
    estado = models.BooleanField(null=False, default=False)