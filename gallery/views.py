from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,'index.html')


def albums_by_category(request,category):
    return render(request,'index.html')  



def albums_by_location(request,location):
    return render(request,'index.html')     


def search_results(request):

    pass
