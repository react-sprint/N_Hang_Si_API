from django.shortcuts import render


def serverstate(request):
    return render(request, 'index.html')
