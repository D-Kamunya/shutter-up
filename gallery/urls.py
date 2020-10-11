from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page,name='homepage'),
    path(r'albums/category/<category>', views.albums_by_category,name='albumcategory'),
]