from django.urls import path
from .views import MyTestingView, UserRegistration


urlpatterns = [
    path('hello/', MyTestingView.as_view(), name='hello'),
    path('register/', UserRegistration.as_view(), name='register'),
]