from enum import unique
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug =models.SlugField(max_length=250, unique=True)
    
    class meta:  
        ordering=('name',)
        verbose_name = 'category'
        verbose_name = plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

class products(models.Model):
   name = models.CharField(max_length=150, unique=True)
   slug = models.SlugField(max_length=250, unique=True)
   img = models.ImageField(upload_to='product')
   desc = models.TextField()
   stock = models.IntegerField()
   available =  models.BooleanField()
   price = models.IntegerField()
   category = models.ForeignKey(categ, on_delete=models.CASCADE)

   def get_url(self):
       return reverse('views',args=[self.category.slug,self.slug])    
    