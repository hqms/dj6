from django.urls import path

from old.views import home, tag, variable

urlpatterns = [
    path('', home, name='home'),
    path('variable', variable, name='variable'),
    path('tags', tag, name='tags'), 
]
