from django.urls import path

from . import views

app_name = 'frontends'
urlpatterns = [
    path('', views.index, name='index'),

    #Services
    path("servicos/s/<slug:slug_services>/", views.front_services, name="front_services"),

    #Institucional
    path("institucional/", views.front_institucional, name="front_institucional"),

    #Links
    path("links/", views.front_links, name="front_links"),

    #Contact
    path("contato/", views.contact, name="contact"),
    path("trabalheconosco/", views.working, name="working"),
]