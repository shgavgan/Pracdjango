from django.db import models

# Create your models here.

class login1(models.Model):
    mail = models.EmailField()
    number = models.IntegerField()

    def __str__(self):
        return self.mail



