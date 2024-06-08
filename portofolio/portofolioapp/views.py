from django.shortcuts import render
from django.views.generic import ListView
from .models import PortModel,ProfileModel

# Create your views here.
class PortHome(ListView):
    model=PortModel
    template_name='home.html'

class PortProfile(ListView):
    model=ProfileModel
    template_name="profile.html"