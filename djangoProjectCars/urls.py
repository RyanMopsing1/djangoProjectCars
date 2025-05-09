"""
URL configuration for djangoProjectCars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from appOfdiller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
path('pokup/',views.pokup.as_view(),name='pokup'),
path('vladelcam/',views.vladelcam.as_view(),name='vladelcam'),

path('vnalichii/',views.vnalichii.as_view(),name='vnalichii'),
path('modelryad/',views.modelryad.as_view(),name='modelryad'),

path('modelryad/<str:title>/<int:pk>/',views.modeldetail.as_view(),name='oneModel'),


]
