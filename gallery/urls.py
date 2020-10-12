from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page,name='home_page'),
    path(r'albums/category/<category>', views.albums_by_category,name='album_category'),
    path(r'albums/location/<location_id>', views.albums_by_location,name='album_location'),
    path(r'search/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)