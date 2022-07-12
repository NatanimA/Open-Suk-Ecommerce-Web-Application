
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from . models import Product,ProductImages,Category,Brand,City
from django.views.generic import (ListView,DetailView,DeleteView,CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from hitcount.views import HitCountDetailView
from django.shortcuts import get_object_or_404
 
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
    

class ProductDetailView(HitCountDetailView,DetailView):
    model = Product
    count_hit = True
    slug_field = 'slug'
    template_name = 'products/product_detail.html'
    slug_field = 'slug'
    context_object_name = 'product_detail'
    
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
    
        context.update({
            
            'popular': Product.objects.order_by('-hit_count_generic__hits')[:3],
            #'product_images': ProductImages.objects.filter(get_object_or_404(Product,)),
        })
        return context


    

    # set to True to count the hit
    

   

class ProductCreate(CreateView):
    model=Product
    fields = ("name","category","quantity","brand","description", "image", "condition")
