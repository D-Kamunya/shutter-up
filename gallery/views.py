from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Category,Location
# Create your views here.

def get_categories():
    return Category.objects.all()

def get_locations():
    return Location.objects.all()

def home_page(request):
    images=Image.get_all_images()


    return render(request,'index.html',{"images":images,"categories":get_categories(),"locations":get_locations()})


def albums_by_category(request,category):
    return render(request,'index.html')  



def albums_by_location(request,location_id):
    return render(request,'index.html')     


def search_results(request):

    pass
