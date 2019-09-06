from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('ask/', views.contact, name='ask'),
    path('about/', views.about, name='about'),
    path('roboclean/', views.roboclean, name='roboclean')
]
