from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings
from django.db import models
from .models import HomeContent,AboutContent,Download,Education,Skill,Description,Certification,Project

class HomeView(TemplateView):
    template_name = 'intro/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = HomeContent.objects.first()
        context['about'] = AboutContent.objects.first()
        context['download'] = Download.objects.last()
        context['education_list'] = Education.objects.all()
        context['skills_list'] = Skill.objects.all()
        context['descriptions'] = Description.objects.all()
        context['certifications_list'] = Certification.objects.all() 
        context['projects_list'] = Project.objects.all()
        context['MEDIA_URL'] = settings.MEDIA_URL
        
        return context

class Error404View(TemplateView):
    template_name = 'intro/error404.html'

    def dispatch(self, request, exception, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.status_code = 404
        return response

class Error500View(TemplateView):
    template_name = 'intro/error500.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        response.status_code = 500
        return response