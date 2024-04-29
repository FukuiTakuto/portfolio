from django.urls import path
from .views import PortHome

urlpatterns = [
    path('home/',PortHome.as_view())
]