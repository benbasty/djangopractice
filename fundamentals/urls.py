from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('basics', views.basics, name = 'basics'),
    path('advanced', views.advanced, name = 'advanced'),
    path('about/<str:name>', views.about, name = 'about')
]