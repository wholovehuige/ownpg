from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to='')

    def __str__(self):
        return self.username

