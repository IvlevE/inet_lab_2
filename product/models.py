from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images/')
# Create your models here.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
