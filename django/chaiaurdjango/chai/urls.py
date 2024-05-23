from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>', views.chai_detail, name='chai_detail'),
]
