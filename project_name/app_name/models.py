from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
