from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.name