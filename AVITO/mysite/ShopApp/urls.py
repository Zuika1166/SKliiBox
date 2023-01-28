from django.urls import path, include
from . import views

app_name = 'ShopApp'
urlpatterns = [
    path('', views.shop_render),
    path('groups/', views.groups_list),
    path('products/', views.products_list),
    path('orders/', views.orders_list, name='orders_list'),
]
