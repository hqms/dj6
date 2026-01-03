from django.urls import path

from old.views import home, variable

urlpatterns = [
    path('', home, name='home'),
    path('variable', variable, name='variable'),
]
