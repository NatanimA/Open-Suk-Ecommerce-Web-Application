from distutils.command.upload import upload
from enum import unique
from itertools import product
from time import timezone
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from accounts.models import CustomUser
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Product(models.Model):
    ###Contains all products information

    CONDITION_TYPE = (
        ("New","New"),
        ("Used","Used")
    )

    name=models.CharField(max_length=100)
    owner = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    city = models.ForeignKey('City',blank=True,null=True,on_delete=models.CASCADE)
    description=models.TextField(blank=True,max_length=500)
    condition=models.CharField(max_length=100,choices=CONDITION_TYPE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(
        upload_to='media/main_products/', blank=True, null=True)
    quantity = models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(default=timezone.now)
    trending=models.BooleanField(default=False,help_text="0=default,1=trending")
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand=models.ForeignKey("Brand",on_delete=models.SET_NULL,null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    slug=models.SlugField(blank = True,null = True)

    def get_absolute_url ( self ) : 
        return reverse ( "products:product_detail" , kwargs= { "slug" : self.slug }) 


    def set_trending_product(self,*args, **kwargs):
        if self.hit_count_generic > 10:
            self.trending=True;
        super(Product, self).set_trending_product(*args, **kwargs)


    def __str__(self) -> str:
        return self.name

    def save(self,*args,**kwargs):
       
        if not self.slug and self.name:
            self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)


class ProductImages(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/products/',blank=True,null=True)

    class Meta:
        
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
    
    def __str__(self) -> str:
        return self.product.name

class Category(models.Model):
    ##Products category
    category_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/category',blank=True,null=True)

    category_slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.category_slug and self.category_name:
            self.category_slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    class Meta:  
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.category_name

class City(models.Model):
    city_name=models.CharField(max_length=50)
    city_slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.city_slug and self.city_name:
            self.city_slug = slugify (self.city_name)
        super(City,self).save(*args, **kwargs)
    def __str__(self) -> str:
        return self.city_name


class Brand(models.Model):
    ##Products Brand
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self) -> str:
        return self.brand_name




