"""nba_draft URL Configuration

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
from django.urls import path
from nbawhoheplayedfor import views

app_name = 'nbawhoheplayedfor'

urlpatterns = [
    path('', views.index, name='index'),
    path('guess/', views.guess, name='guess'),
    path('result/', views.result, name='result'),
    path('nbawhoheplayedfor/', include('nbawhoheplayedfor.urls'))

]
