from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Person
from .forms import ContactForm
from django.shortcuts import redirect
from django.conf import settings

class HomeView(TemplateView):
    template_name = 'intro/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['MEDIA_URL'] = settings.MEDIA_URL
        return context

    
