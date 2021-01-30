from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Id(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name