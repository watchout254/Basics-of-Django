from django.shortcuts import render


# Create your views here.

def emobilis(request):
    return render(request, 'index.html')
