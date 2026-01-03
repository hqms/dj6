from django.shortcuts import render

def partial(request):
    context = {
        'name': 'Django6',
        'age'  : 30,
    }
    return render(request, 'new/partial.html', context)