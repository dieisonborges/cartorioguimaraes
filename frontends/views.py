from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from backends.models import Links, Services, Institutionals, Archives

# Create your views here.
def index(request):    
    template_name = 'frontends/index.html'
    services = Services.objects.order_by('-created_at')
    context = {
        'services': services,
    }
    return render(request, template_name, context)

#Services
def front_services(request, slug_services):
    template_name = 'services/front.html'
    services = Services.objects.filter(slug=slug_services)    
    for service in services:
        pass
    services_list = Services.objects.order_by('-created_at')
    context = {
        'service': service, 
        'services': services_list
    }
    return render(request, template_name, context)

#Institucional
def front_institucional(request):
    template_name = 'institucionals/front.html'
    services = Services.objects.order_by('-created_at')

    principals = Institutionals.objects.filter(slug='principal')[:1]  
    for principal in principals:
        pass 

    missaos = Institutionals.objects.filter(slug='missao')[:1] 
    for missao in missaos:
        pass

    visaos = Institutionals.objects.filter(slug='visao')[:1] 
    for visao in visaos:
        pass

    valoress = Institutionals.objects.filter(slug='valores')[:1] 
    for valores in valoress:
        pass
    
    context = {
        'principal': principal, 
        'missao': missao,
        'visao': visao,
        'valores': valores,
        'services': services
    }

    return render(request, template_name, context)

#Links
def front_links(request):    
    services = Services.objects.order_by('-created_at')
    template_name = 'links/front.html'
    links = Links.objects.order_by('-created_at')
    context = {
        'links': links,
        'services': services
    }    
    return render(request, template_name, context)

#Archives
def front_archives(request):    
    services = Services.objects.order_by('-created_at')

    archives = Archives.objects.order_by('-created_at')
    template_name = 'archives/front.html'

    context = {
        'archives': archives,
        'services': services
    }    
    return render(request, template_name, context)

#Contato
def contact(request):    
    services = Services.objects.order_by('-created_at')
    template_name = 'contact/contact.html'
    context = {
        'services': services
    }    
    return render(request, template_name, context)

def working(request):    
    services = Services.objects.order_by('-created_at')
    template_name = 'contact/working.html'
    context = {
        'services': services
    }    
    return render(request, template_name, context)
