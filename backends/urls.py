from django.urls import path

from . import views

app_name = 'backends'
urlpatterns = [
    #INDEX
    path('', views.index, name='index'),

    #LOGIN
    path('login/', views.login_man, name='login_man'),
    path('logout/', views.logout_man, name='logout_man'),

    #USERS
    path('usuarios/', views.index_users, name='index_users'),
    path('usuarios/criar/', views.create_users, name='create_users'),
    path('usuarios/alterar/<int:user_id>/', views.update_users, name='update_users'),
    path('usuarios/apagar/<int:user_id>/', views.delete_users, name='delete_users'),
    path('usuarios/senha/', views.password_users, name='password_users'),

    #LINKS
    path("links/", views.index_links, name="index_links"),
    path("links/criar/", views.create_links, name="create_links"),
    #path("links/ver/<int:link_id>/", views.read_links, name="read_links"),
    path("links/alterar/<int:link_id>/", views.update_links, name="update_links"),
    path("links/apagar/<int:link_id>/", views.delete_links, name="delete_links"),  

    #Services
    path("servicos/", views.index_services, name="index_services"), #list
    path("servicos/criar/", views.create_services, name="create_services"),
    #path("servicos/<int:service_id>/", views.read_services, name="read_services"),
    path("servicos/alterar/<int:service_id>/", views.update_services, name="update_services"),
    path("servicos/apagar/<int:service_id>/", views.delete_services, name="delete_services"),    

    #Institucional
    path("institucional/alterar/<slug:slug_institucional>/", views.update_institucional, name="update_institucional"),

    #Archives
    path("modelos/", views.index_archives, name="index_archives"),
    path("modelos/criar/", views.create_archives, name="create_archives"),
    path("modelos/alterar/<int:archive_id>/", views.update_archives, name="update_archives"),
    path("modelos/apagar/<int:archive_id>/", views.delete_archives, name="delete_archives"),

]