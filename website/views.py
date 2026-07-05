from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class AchievementsView(TemplateView):
    template_name = 'achievements.html'

class ResourcesView(TemplateView):
    template_name = 'resources.html'

class TeamView(TemplateView):
    template_name = 'team.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
