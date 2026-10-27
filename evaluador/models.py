from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True)
# Create your models here.
