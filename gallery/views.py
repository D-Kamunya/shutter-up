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
    images=Image.search_image(category)
    return render(request,'browser.html',{"tag":'categories',"images":images,"category":category,"categories":get_categories(),"locations":get_locations()})   



def albums_by_location(request,location_id):

    images=Image.filter_by_location(location_id)
    location=Location.objects.get(pk=location_id)
    return render(request,'browser.html',{"tag":'locations',"images":images,"location":location,"categories":get_categories(),"locations":get_locations()})     


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": images,"categories":get_categories(),"locations":get_locations()})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message,"categories":get_categories(),"locations":get_locations()})




  
