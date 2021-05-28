from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone




class SpecialismLogo(models.Model):
    specialism_logo_name = models.CharField(max_length=30)
    specialism_file = models.FileField()

    def __str__(self):
        return self.specialism_logo_name + " logo"

class Specialism(models.Model):
    specialism_name = models.CharField(max_length=30)
    specialism_logo = models.ForeignKey(SpecialismLogo, on_delete=models.CASCADE)


    def __str__(self):
        return self.specialism_name


class BackgroundImage(models.Model):
    background_file = models.FileField()
    specialism = models.ForeignKey(Specialism, on_delete=models.CASCADE)

    def __str__(self):
        return self.specialism.specialism_name + " " + self.background_file.name
