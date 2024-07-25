from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls')),
    path('', views.product_list, name='product-list'),
]
