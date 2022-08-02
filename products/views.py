
from urllib import response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from requests import request
from django.views.generic.edit import FormView
from .forms import ConsumerRegistrationForm, ProductForm, ProductImagesForm
from . models import Product,ProductImages,Category,Brand,City
from django.views.generic.edit import CreateView

from django.views.generic import (ListView,DetailView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from hitcount.views import HitCountDetailView
from django.shortcuts import get_object_or_404
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

 
def productList(request,category_slug=None,city_slug=None):
    category=None
    city=None
    productList=Product.objects.all()
    categoryList=Category.objects.annotate(total_products=Count('product'))
    cityList=City.objects.all()
   
    if city_slug and not category_slug:
        city = City.objects.get(city_slug=city_slug)
        productList = productList.filter(city=city)
    
    if category_slug and not city_slug:
        category = Category.objects.get(category_slug=category_slug)
        productList=productList.filter(category=category)
    
    



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



    paginator=Paginator(productList,10)
    page = request.GET.get('page')
    product_list =paginator.get_page(page)
    template = 'products/product_list.html'

    context = {'product_list' : productList , 'category_list': categoryList, 'category' :category,'cityList':cityList,'city':city}
    return render(request,template,context)
    

class ProductDetailView(HitCountDetailView,DetailView):
    model = Product
    # set to True to count the hit
    count_hit = True
    slug_field = 'slug'
    template_name = 'products/product_detail.html'
    slug_field = 'slug'
    context_object_name = 'product_detail'
    
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
    
        context.update({
            
            'popular': Product.objects.order_by('-hit_count_generic__hits')[:3],
            'product_images': ProductImages.objects.filter(product_id = self.object.id),
        })
        return context


class ProductCreate(LoginRequiredMixin, CreateWithInlinesView):
    model=Product
    form_class=ProductForm
    template_name = 'products/product_form.html'
    #inlines = [ProductImagesForm]
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('products:product_list')

   
    