
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from . models import Product,ProductImages,Category,Brand,City
from django.views.generic import (ListView,DetailView,DeleteView,CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
 
def productList(request,category_slug=None,city_slug=None):
    category=None
    city=None
    productList=Product.objects.all()
    categoryList=Category.objects.annotate(total_products=Count('product'))
   
    
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        productList=productList.filter(category=category)
    
    if city_slug:
        city = City.objects.get(slug=city_slug)
        productList=productList.filter(city=city)



    search_query = request.GET.get('q')
    if search_query:
        productList = productList.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(price__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains=search_query) |
            Q(category__category_name__icontains=search_query) |
            Q(city__city_name__icontains = search_query)

        )



    paginator=Paginator(productList,5)
    page = request.GET.get('page')
    product_list =paginator.get_page(page)
    template = 'products/product_list.html'

    context = {'product_list' : productList , 'category_list': categoryList, 'category' :category}
    return render(request,template,context)
    

def productDetail(request,product_slug):

    productdetail = Product.objects.get(slug=product_slug)
    productimages= ProductImages.objects.filter(product=productdetail)
    template='products/product_detail.html'

    context ={'product_detail':productdetail,'product_images':productimages}

    return render(request,template,context)

class ProductCreate(CreateView):
    model=Product
    fields = ("name","category","quantity","brand","description", "image", "condition")
