from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def variable(request):
    context = {'username': 'Hakim', 
               'user':{
                    'first_name': 'Hakim',
                    'age': 30,
                }}
    
    return render(request, 'variable.html', context)

def tag(request):
    context = {
        'items': ['Item 1', 'Item 2', 'Item 3'],
        'user': {
                'is_authenticated': True,
                'first_name': 'Hakim'
            }
        }
    return render(request, 'tags.html', context=context)

def filter(request):
    context = {
        'text': '  Hello, Welcome to Django Template Filters!  ',        
    }
    return render(request, 'filters.html', context)