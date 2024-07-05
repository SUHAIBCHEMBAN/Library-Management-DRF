from django.urls import path
from .views import UserRegistrationView, CustomTokenObtainPairView

urlpatterns = [
    # user register
    path('register/', UserRegistrationView.as_view(), name='register'),
    # user login
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]
