from django.urls import path

from old.views import home, tag, variable, filter

urlpatterns = [
    path('', home, name='home'),
    path('variable', variable, name='variable'),
    path('tags', tag, name='tags'), 
    path('filter', filter, name='filter'),
]
