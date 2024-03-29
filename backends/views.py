from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.text import slugify
from django.db import IntegrityError


from .forms import InstitucionalForm, ArchiveForm, CategoryArchiveForm
from .forms import UserForm, UserFormUpdate, LinksForm, ServicesForm

from .models import Links, Services, Institutionals, Archives, CategoryArchives

# Create your views here.

#LOGIN
def login_man(request):
    template_name = 'login/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')  
            return HttpResponseRedirect(reverse('backends:index'))
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return render(request, template_name, {})

@login_required
def logout_man(request):
    logout(request)
    return redirect('backends:login_man')

#Index
@login_required
def index(request):    
    template_name = 'backends/index.html'
    context = {
        
    }
    return render(request, template_name, context)

#Users
@login_required
def index_users(request):
    template_name = 'users/index.html'
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, template_name, context)

def create_users(request):
    template_name = 'users/create_update.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Adicionado com sucesso!')        
            return HttpResponseRedirect(reverse('backends:index_users'))
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)

def update_users(request, user_id):
    template_name = 'users/create_update.html'
    user = User.objects.get(pk=user_id)
    context = {}
    if request.method == 'POST':
        form = UserFormUpdate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_users'))
        else:
            messages.error(request, 'Houve um erro!')   
    form = UserFormUpdate(instance=user)
    context['form'] = form
    return render(request, template_name, context)

def delete_users(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'Removido com sucesso!')        
    return HttpResponseRedirect(reverse('backends:index_users'))

def password_users(request):
    template_name = 'users/password.html'    
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Aletrado com sucesso!')        
            return HttpResponseRedirect(reverse('backends:index'))
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)

#Links
@login_required
def index_links(request):    
    template_name = 'links/index.html'
    links = Links.objects.all().order_by('description')
    context = {
        'links': links,
    }
    return render(request, template_name, context)

@login_required
def create_links(request):
    template_name = 'links/create_update.html'
    context = {}
    if request.method == 'POST':
        form = LinksForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_links'))
    form = LinksForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def read_links(request):    
    pass

@login_required
def update_links(request, link_id):
    template_name = 'links/create_update.html'
    context = {}
    link = get_object_or_404(Links, id=link_id)
    if request.method == 'POST':
        form = LinksForm(request.POST, request.FILES, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modificado com sucesso!')        
            return HttpResponseRedirect(reverse('backends:index_links'))
    else:        
        form = LinksForm(instance=link)
        context['form'] = form
    return render(request, template_name, context)
    
@login_required
def delete_links(request, link_id):
    links = get_object_or_404(Links, id=link_id)
    links.delete()
    messages.success(request, 'Removido com sucesso!')        
    return HttpResponseRedirect(reverse('backends:index_links'))

#Services
@login_required
def index_services(request):    
    template_name = 'services/index.html'
    services = Services.objects.order_by('-created_at')
    context = {
        'services': services,
    }
    return render(request, template_name, context)

@login_required
def create_services(request):
    template_name = 'services/create_update.html'
    context = {}
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.slug = slugify(f.name)
            f.save()
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_services'))
    form = ServicesForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def read_services(request):    
    pass

@login_required
def update_services(request, service_id):
    template_name = 'services/create_update.html'
    context = {}
    service = get_object_or_404(Services, id=service_id)
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            f = form.save(commit=False)
            f.slug = slugify(f.name)
            f.save()
            messages.success(request, 'Modificado com sucesso!')        
            return HttpResponseRedirect(reverse('backends:index_services'))
    else:        
        form = ServicesForm(instance=service)
        context['form'] = form
    return render(request, template_name, context)
    
@login_required
def delete_services(request, service_id):
    services = get_object_or_404(Services, id=service_id)
    services.delete()
    messages.success(request, 'Removido com sucesso!')        
    return HttpResponseRedirect(reverse('backends:index_services'))

#Institucional
@login_required
def update_institucional(request, slug_institucional):
    ## Slug Fixed
    #principal
    #missao
    #visao
    #valores
    template_name = 'institucional/create_update.html'
    context = {}
    institucional = Institutionals.objects.get(slug=slug_institucional)
    if request.method == 'POST':
        form = InstitucionalForm(request.POST, instance=institucional)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            messages.success(request, 'Modificado com sucesso!')        
            return HttpResponseRedirect(reverse('backends:index'))
    else:        
        form = InstitucionalForm(instance=institucional)
        context['form'] = form
    return render(request, template_name, context)

#Archives
@login_required
def index_archives(request):
    template_name = 'archives/index.html'
    archives = Archives.objects.all().order_by('name')
    context = {
        'archives': archives,
    }
    return render(request, template_name, context)  

@login_required
def create_archives(request):
    template_name = 'archives/create_update.html'
    context = {}
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_archives'))
    form = ArchiveForm()
    context['form'] = form
    return render(request, template_name, context) 

@login_required
def update_archives(request, archive_id):
    template_name = 'archives/create_update.html'
    context = {}
    archive = get_object_or_404(Archives, id=archive_id)
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES, instance=archive)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_archives'))
    else:        
        form = ArchiveForm(instance=archive)
        context['form'] = form
    return render(request, template_name, context) 

@login_required
def delete_archives(request, archive_id):
    archives = get_object_or_404(Archives, id=archive_id)
    if archives.docfile:        
        archives.docfile.delete(save=True)
    archives.delete()
    messages.success(request, 'Removido com sucesso!')        
    return HttpResponseRedirect(reverse('backends:index_archives'))

#Category Archives
@login_required
def index_category_archives(request):
    template_name = 'archives/index_category.html'
    category_archives = CategoryArchives.objects.all().order_by('-mother_category')
    context = {
        'category_archives': category_archives,
    }
    return render(request, template_name, context)  

@login_required
def create_category_archives(request):
    template_name = 'archives/create_update_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_category_archives'))
    form = CategoryArchiveForm()
    context['form'] = form
    return render(request, template_name, context) 

@login_required
def update_category_archives(request, category_archive_id):
    template_name = 'archives/create_update_category.html'
    context = {}
    archive = get_object_or_404(CategoryArchives, id=category_archive_id)
    if request.method == 'POST':
        form = CategoryArchiveForm(request.POST, request.FILES, instance=archive)
        if form.is_valid():
            form.save()            
            messages.success(request, 'Adicionado com sucesso!')
            return HttpResponseRedirect(reverse('backends:index_category_archives'))
    else:        
        form = CategoryArchiveForm(instance=archive)
        context['form'] = form
    return render(request, template_name, context) 

@login_required
def delete_category_archives(request, category_archive_id):
    archives = get_object_or_404(CategoryArchives, id=category_archive_id)
    try:
        archives.delete()
        messages.success(request, 'Removido com sucesso!')        
        return HttpResponseRedirect(reverse('backends:index_category_archives'))
    except IntegrityError:
        messages.error(request, 'Está é uma categoria mãe!')        
        return HttpResponseRedirect(reverse('backends:index_category_archives'))