from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_category(request, category):
    return HttpResponse(f'Категория {category}')