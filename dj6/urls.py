from django.urls import path

from new.views import partial
from old.views import comment, home, tag, variable, filter

urlpatterns = [
    path('', home, name='home'),
    path('variable', variable, name='variable'),
    path('tags', tag, name='tags'), 
    path('filter', filter, name='filter'),
    path('comment', comment, name='comment'),
    path('partial', partial, name='partial'),
]
