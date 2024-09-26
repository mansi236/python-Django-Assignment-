from django.contrib import admin
from django.urls import path
from webPage import views
urlpatterns = [
    path('form',views.home,name="homePage"),
    path('userInfo',views.user_Info,name="userInfo"),
]