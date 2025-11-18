import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'competencia03.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Empresa

print("=" * 50)
print("VERIFICAÇÃO DE USUÁRIOS")
print("=" * 50)

print(f"\nTotal de usuários: {User.objects.count()}")
print(f"Usuários staff (is_staff=True): {User.objects.filter(is_staff=True).count()}")
print(f"Superusuários (is_superuser=True): {User.objects.filter(is_superuser=True).count()}")

print("\n" + "=" * 50)
print("LISTA DE USUÁRIOS:")
print("=" * 50)

for user in User.objects.all().order_by('id'):
    print(f"ID: {user.id} | Username: {user.username}")
    print(f"  - is_staff: {user.is_staff}")
    print(f"  - is_superuser: {user.is_superuser}")
    print(f"  - Nome: {user.first_name} {user.last_name}")
    print()

print("=" * 50)
print("EMPRESAS E SEUS MEMBROS:")
print("=" * 50)

for empresa in Empresa.objects.all():
    print(f"\nEmpresa: {empresa.nome}")
    print(f"  Criador: {empresa.criador.username}")
    print(f"  Membros: {empresa.membros.count()}")
    for membro in empresa.membros.all():
        print(f"    - {membro.username}")
