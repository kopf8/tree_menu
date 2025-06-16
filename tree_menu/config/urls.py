from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='menu_demo/index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='menu_demo/about.html'), name='about'),
    path('about/contacts/', TemplateView.as_view(template_name='menu_demo/contacts.html'),
          name='contacts'),
    path('about/team/', TemplateView.as_view(template_name='menu_demo/team.html'),
          name='team'),
    path('about/team/vacancies/', TemplateView.as_view(template_name='menu_demo/vacancies.html'),
          name='vacancies'),
]
