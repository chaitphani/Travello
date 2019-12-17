from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 30, null=True, blank=True)
    last_name  = models.CharField(max_length = 30, null=True, blank=True)
    email      = models.EmailField(max_length = 30, null=True, blank=True)
    username   = models.CharField(max_length = 30, null=True, blank=True)
    mob        = models.CharField(max_length = 10)
    password = models.CharField(max_length=8, null=False, blank=False)
    image = models.FileField()
    

    def __str__(self):
        return self.username



