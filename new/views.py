from django.shortcuts import render

def partial(request):
    context = {
        'name': 'Django6',
        'age'  : 30,
    }
    return render(request, 'new/partial.html', context)

def direct_access(request):
    context = {
        'name': 'Direct Access',
        'age'  : 30,
    }
    return render(request, 'new/direct_access.html', context=context)