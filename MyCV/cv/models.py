from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    summary = models.TextField()
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
