from django.db import models


class FirstPage(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

# Create your models here.
