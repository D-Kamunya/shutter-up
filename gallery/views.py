from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
# Create your views here.
def home_page(request):
    images=Image.get_all_images()
    print(images)
    return render(request,'index.html',{"images":images})


def albums_by_category(request,category):
    return render(request,'index.html')  



def albums_by_location(request,location):
    return render(request,'index.html')     


def search_results(request):

    pass
