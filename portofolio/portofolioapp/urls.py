from django.urls import path
from .views import PortHome,PortProfile

urlpatterns = [
    path('home/',PortHome.as_view()),
    path('profile/',PortProfile.as_view(),name="profile")
]