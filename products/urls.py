from django.urls import path
from . import views 

app_name='products'

urlpatterns = [
    path('',views.productList,name='product_list'),
    path('<slug:category_slug>', views.productList, name='product_list_category'),
    path('products/<slug:product_slug>/',views.productDetail ,name='product_detail'),
    # path('',views.ProductDelete.as_view(),name='product_delete'),
]

