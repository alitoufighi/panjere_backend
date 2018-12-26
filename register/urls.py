
from django.urls import path
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('register', views.accept),
    path('', TemplateView.as_view(template_name='home.html')),
]
