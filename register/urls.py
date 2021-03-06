
from django.urls import path
from .import views
from django.views.generic import TemplateView


urlpatterns = [
    path('panjere/register', views.accept),
    path('panjere/', TemplateView.as_view(template_name='home.html')),
    path('panjere/export', views.export_attendants_csv, name='export_attendants_csv'),
]
