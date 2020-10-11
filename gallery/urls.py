from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page,name='homepage'),
    path(r'albums/category/<category>', views.albums_by_category,name='albumcategory'),
    path(r'albums/location/<location>', views.albums_by_location,name='albumlocation'),
    path(r'search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)