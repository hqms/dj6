from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def variable(request):
    context = {'username': 'Hakim'}
    return render(request, 'variable.html', context)