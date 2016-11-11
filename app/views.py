from django.shortcuts import render

from django.views.generic import TemplateView, CreateView
from app.models import Location
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_list'] = Location.objects.all()
        return context

class LocationCreateView(CreateView):
    model = Location
    fields = ('lat', 'lng')
    success_url = reverse_lazy('index_view')
