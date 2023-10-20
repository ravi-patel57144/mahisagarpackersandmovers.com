from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True, default='Mahisagar Packers and Movers')
    category = models.CharField(max_length=50, null=True, blank=True, default='Branch Office')
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(default='info@mahisagarpackersandmovers.com')


class Pages(models.Model):
    city = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = verbose_name + 's'

class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=12)
    date = models.DateField()
    s_from = models.CharField(max_length=50)
    s_to = models.CharField(max_length=50)
    message = models.TextField()
    reviewed = models.BooleanField(default=False)