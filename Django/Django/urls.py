"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^poll/', include('cna440.urls')), #this line added
    url(r'^boot/', include('bootsrap_main.urls')),#bootline
    url(r'^animate/', include('animate.urls')),#animate line
    url(r'^admin/', admin.site.urls),
    url(r'^', include('static_host.urls')),
    url(r'^polls/', include('static_host.urls')), #this line added
]