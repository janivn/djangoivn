from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    content_objective_name = 'home'
    template_name = "home.html"