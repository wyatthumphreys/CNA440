from django.shortcuts import render
from django.http import HttpResponse


def animatereturn(request):
    return render(request, 'animate.html')