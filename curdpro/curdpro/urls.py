"""curdpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from curdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeview),
    path('home',views.homeview,name='home'),
    path('form',views.formview,name='form'),
    path('datet',views.dateview,name='datet'),
    path('cdd/<id>',views. dateentryview,name='cdd'),
    path('update/<id>',views.updateview,name='update'),
    path('updating_data/<id>',views.updating_data,name='updating_data'),
    path('delete/<id>',views. deleteview,name='delete'),
    path('update',views.updateviews,name='update'),
    path('updated/<id>',views.updatingview,name='updated')

]
