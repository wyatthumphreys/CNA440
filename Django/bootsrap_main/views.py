from django.shortcuts import render
from django.http import HttpResponse


def bootreturn(request):
    return render(request, 'bootstrap.html')
