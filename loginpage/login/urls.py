from django.urls import path
from . import views

urlpatterns = [

    path('',views.loginpage.as_view(),name="index"),
    path('data',views.data),
    path('index',views.loginpage.as_view(),name="index"),

]
