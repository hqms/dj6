from django.urls import path

from old.views import home

urlpatterns = [
    path('', home, name='home'),
]
