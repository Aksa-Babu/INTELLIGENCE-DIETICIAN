"""intellidiet URL Configuration

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
from dietapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('adminhome',views.adminhome),
    path('adminuser',views.adminuser),
    path('adminex',views.adminex),
    path('adminraw',views.adminraw),
    path('admincooked',views.admincooked),
    path('userhome',views.userhome),
    path('experthome',views.experthome),
    path('superhome',views.superhome),
    path('expreg',views.expreg),
    path('expertvreq',views.expertvreq),
    path('exppyramid',views.exppyramid),
    path('inchat',views.inchat),
    path('sfChatPer',views.sfChatPer),
    path('usercooked',views.usercooked),
    path('userraw',views.userraw),
    path('userexercise',views.userexercise),
    path('userreq',views.userreq),
    path('userviewreq',views.userviewreq),
    path('userfeed',views.userfeed),
    path('superfeed',views.superfeed),
    path('userpyramid',views.userpyramid),
]
