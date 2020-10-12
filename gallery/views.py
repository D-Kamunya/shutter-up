from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Category
# Create your views here.

def get_categories():
    return Category.objects.all()

def home_page(request):
    images=Image.get_all_images()
    categories=get_categories()
    return render(request,'index.html',{"images":images,"categories":categories})


def albums_by_category(request,category):
    return render(request,'index.html')  



def albums_by_location(request,location):
    return render(request,'index.html')     


def search_results(request):

    pass
