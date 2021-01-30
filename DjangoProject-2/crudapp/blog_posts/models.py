from django.db import models
from django.urls import reverse


# Create your models here.

class Table(models.Model):
    Name = models.CharField(max_length=30)
    # T_size = models.IntegerField()
    # T_width = models.IntegerField()
    # Date_of_Delivery = models.DateField()
    Quantity = models.IntegerField()
    Address = models.CharField(max_length=70)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('table_edit', kwargs={'pk': self.pk})
