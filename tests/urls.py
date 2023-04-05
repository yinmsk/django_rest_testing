from django.urls import path
from .views import MyTestingView

urlpatterns = [
    path('', MyTestingView.as_view(), name='testing'),
]