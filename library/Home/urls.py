from django.urls import path
from . import views

urlpatterns = [

    # Show the Running Message
    path('',views.Home.as_view(),name='Home'),   

]


