from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('user_data/', InstaScrapeView.as_view()),
]