from django.urls import path
from .views import (
    HomeView, AboutView, AchievementsView, 
    ResourcesView, TeamView, ContactView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('achievements/', AchievementsView.as_view(), name='achievements'),
    path('resources/', ResourcesView.as_view(), name='resources'),
    path('team/', TeamView.as_view(), name='team'),
    path('contact/', ContactView.as_view(), name='contact'),
]
