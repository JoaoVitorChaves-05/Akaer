from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Empresas
    path("empresas/criar/", views.criar_empresa, name="criar_empresa"),
    path("empresas/<int:id>/", views.empresa_view, name="empresa"),
    path("empresas/<int:id>/delete/", views.delete_empresa, name="delete_empresa"),
    path("empresas/<int:empresa_id>/adicionar-membro/", views.adicionar_membro_empresa, name="adicionar_membro_empresa"),
    path("empresas/<int:empresa_id>/remover-membro/<int:user_id>/", views.remover_membro_empresa, name="remover_membro_empresa"),

    # Projetos
    path("empresas/<int:empresa_id>/projetos/criar/", views.criar_projeto, name="criar_projeto"),
    path("projetos/<int:id>/", views.projeto_view, name="projeto"),
    path("projetos/<int:id>/delete/", views.delete_projeto, name="delete_projeto"),
    path("projetos/<int:id_projeto>/adicionar-membro/", views.add_membro, name="add_membro"),
    path("projetos/<int:id_projeto>/remover-membro/<int:id_usuario>/", views.remove_membro, name="remove_membro"),
    
    # Usuários (apenas superusuários)
    path("usuarios/", views.usuarios_list, name="usuarios_list"),
    path("usuarios/criar/", views.usuario_create, name="usuario_create"),
    path("usuarios/<int:id>/editar/", views.usuario_edit, name="usuario_edit"),
    path("usuarios/<int:id>/deletar/", views.usuario_delete, name="usuario_delete"),
]
