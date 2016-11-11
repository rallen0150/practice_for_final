from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from app.models import Location
from django.urls import reverse_lazy


class IndexView(TemplateView):
    model = Location
    template_name = 'index.html'

class LocationCreateView(CreateView):
    model = Location
    fields = ('lat', 'lng')
    success_url = reverse_lazy('index_view')
