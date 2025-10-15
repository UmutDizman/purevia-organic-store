
from django.urls import path
from . import views

app_name = 'purevia'



urlpatterns = [
    path("", views.index, name="index"),

]