from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from .models import Empresa, Projeto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, "login.html")

@login_required
def dashboard(request):
    empresas = (Empresa.objects.filter(criador=request.user) |
                Empresa.objects.filter(membros=request.user)).distinct()

    return render(request, "dashboard.html", {"empresas": empresas})

@login_required
def empresa_view(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    
    if empresa.criador != request.user and request.user not in empresa.membros.all():
        return HttpResponseForbidden("Você não tem acesso a esta empresa.")

    if empresa.criador == request.user:
        projetos = empresa.projetos.all()
    else:
        projetos = empresa.projetos.filter(
            Q(criador=request.user) | Q(membros=request.user)
        ).distinct()
    
    usuarios_disponiveis = User.objects.exclude(
        id__in=empresa.membros.values_list('id', flat=True)
    ).exclude(id=empresa.criador.id).exclude(
        Q(empresas_vinculadas__isnull=False) | Q(empresas_criadas__isnull=False)
    ).exclude(is_superuser=True).order_by('username')

    return render(request, "empresas/empresa.html", {
        "empresa": empresa,
        "projetos": projetos,
        "usuarios_disponiveis": usuarios_disponiveis
    })

@login_required
def delete_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    if empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador pode excluir esta empresa.")
    empresa.delete()
    return redirect('dashboard')

@login_required
def delete_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if projeto.criador != request.user and projeto.empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador do projeto ou dono da empresa pode excluí-lo.")
    projeto.delete()
    return redirect('empresa', id=projeto.empresa.id)

@login_required
def add_membro(request, id_projeto):
    projeto = get_object_or_404(Projeto, id=id_projeto)
    if projeto.criador != request.user and projeto.empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador do projeto ou dono da empresa pode adicionar membros.")

    user_id = request.POST["user_id"]
    usuario = User.objects.get(id=user_id)
    projeto.membros.add(usuario)

    return redirect('projeto', id=id_projeto)

@login_required
def remove_membro(request, id_projeto, id_usuario):
    projeto = get_object_or_404(Projeto, id=id_projeto)
    if projeto.criador != request.user and projeto.empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador do projeto ou dono da empresa pode remover membros.")

    usuario = User.objects.get(id=id_usuario)
    projeto.membros.remove(usuario)

    return redirect('projeto', id=id_projeto)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def criar_empresa(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("Apenas usuários habilitados como donos de empresa podem criar empresas.")
    
    if request.method == "POST":
        nome = request.POST["nome"]
        empresa = Empresa.objects.create(
            nome=nome,
            criador=request.user
        )

        return redirect('dashboard')
    
    return render(request, "empresas/criar.html")

@login_required
def criar_projeto(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    if empresa.criador != request.user and request.user not in empresa.membros.all():
        return HttpResponseForbidden("Apenas o criador ou membros da empresa podem adicionar projetos.")
    
    if request.method == "POST":
        nome = request.POST["nome"]
        projeto = Projeto.objects.create(
            nome=nome,
            empresa=empresa,
            criador=request.user
        )
        return redirect('empresa', id=empresa_id)
    
    return render(request, "projetos/criar.html", {"empresa": empresa})

@login_required
def adicionar_membro_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    if empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador da empresa pode adicionar membros.")
    
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        if user_id:
            usuario = get_object_or_404(User, id=user_id)
            empresa.membros.add(usuario)
    
    return redirect('empresa', id=empresa_id)

@login_required
def remover_membro_empresa(request, empresa_id, user_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    
    if empresa.criador != request.user:
        return HttpResponseForbidden("Apenas o criador da empresa pode remover membros.")
    
    usuario = get_object_or_404(User, id=user_id)
    empresa.membros.remove(usuario)
    
    return redirect('empresa', id=empresa_id)

@login_required
def projeto_view(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    
    if (projeto.criador != request.user and 
        request.user not in projeto.membros.all() and 
        projeto.empresa.criador != request.user):
        return HttpResponseForbidden("Você não tem acesso a este projeto.")
    
    usuarios_disponiveis = projeto.empresa.membros.exclude(
        id__in=projeto.membros.values_list('id', flat=True)
    ).exclude(id=projeto.criador.id)
    
    if projeto.empresa.criador.id != projeto.criador.id and projeto.empresa.criador not in projeto.membros.all():
        usuarios_disponiveis = usuarios_disponiveis | User.objects.filter(id=projeto.empresa.criador.id)
    
    usuarios_disponiveis = usuarios_disponiveis.order_by('username')
    
    return render(request, "projetos/projeto.html", {
        "projeto": projeto,
        "usuarios_disponiveis": usuarios_disponiveis
    })

# CRUD de Usuários (apenas para superusuários)
@login_required
def usuarios_list(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Apenas administradores podem acessar esta página.")
    
    usuarios = User.objects.all().order_by('-date_joined')
    return render(request, "usuarios/list.html", {"usuarios": usuarios})

@login_required
def usuario_create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Apenas administradores podem criar usuários.")
    
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST.get("email", "")
        password = request.POST["password"]
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        is_staff = request.POST.get("is_staff") == "on"
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff
        )
        return redirect('usuarios_list')
    
    return render(request, "usuarios/create.html")

@login_required
def usuario_edit(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Apenas administradores podem editar usuários.")
    
    usuario = get_object_or_404(User, id=id)
    
    if request.method == "POST":
        usuario.username = request.POST["username"]
        usuario.email = request.POST.get("email", "")
        usuario.first_name = request.POST.get("first_name", "")
        usuario.last_name = request.POST.get("last_name", "")
        usuario.is_staff = request.POST.get("is_staff") == "on"
        
        if request.POST.get("password"):
            usuario.set_password(request.POST["password"])
        
        usuario.save()
        return redirect('usuarios_list')
    
    return render(request, "usuarios/edit.html", {"usuario": usuario})

@login_required
def usuario_delete(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Apenas administradores podem deletar usuários.")
    
    usuario = get_object_or_404(User, id=id)
    
    if usuario.is_superuser:
        return HttpResponseForbidden("Não é possível deletar um superusuário.")
    
    if request.method == "POST":
        usuario.delete()
        return redirect('usuarios_list')
    
    return render(request, "usuarios/delete.html", {"usuario": usuario})