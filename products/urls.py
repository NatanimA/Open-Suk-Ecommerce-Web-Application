from django.urls import path
from . import views 

app_name='products'

urlpatterns = [
    path('',views.productList,name='product_list'),
    
    path('cities/<slug:city_slug>',views.productList,name='product_list_city'),
    path('products/<slug:slug>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('post/new/',views.ProductCreate.as_view(),name='post'),
    path('categories/<slug:category_slug>', views.productList, name='product_list_category'),
    # path('',views.ProductDelete.as_view(),name='product_delete'),
]

