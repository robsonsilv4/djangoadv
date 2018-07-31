from django.urls import path
from .views import home, my_logout, HomePageView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('home/', home, name='home'),
    path('logout/', my_logout, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html')),
    path('home3/', HomePageView.as_view())
]
