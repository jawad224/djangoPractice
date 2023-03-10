from django.db import models

# Create your models here.


class About (models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
