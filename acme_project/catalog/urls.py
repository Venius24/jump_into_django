from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('<slug:category>/', views.product_detail, name="product_detail"),
    path("", views.product_list, name="product_list")
] 