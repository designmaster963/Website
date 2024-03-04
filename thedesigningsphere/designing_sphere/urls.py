from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('contact',views.contact, name = 'contact'),
    path('about',views.about, name = 'about'),
    path('club',views.club, name = 'club'),
    path('projects',views.projects, name = 'projects'),
    path('team',views.team, name = 'team'),
    path('post_create/', views.post_create, name='post_create'),
]