# 🚀 Teste Técnico - Akaer Estágio

Repositório contendo as soluções para o processo seletivo de estágio na **Akaer Engineering**. O teste está dividido em três competências que avaliam diferentes habilidades técnicas essenciais para a vaga.

---

## 📋 Índice

- [Competência 01 - Algoritmos e Análise de Dados](#competência-01---algoritmos-e-análise-de-dados)
- [Competência 02 - Banco de Dados SQL](#competência-02---banco-de-dados-sql)
- [Competência 03 - Sistema de Gestão com Django](#competência-03---sistema-de-gestão-com-django)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar](#como-executar)

---

## 📚 Competência 01 - Algoritmos e Análise de Dados

Nesta competência foram resolvidos **dois desafios de programação competitiva** (judges) e **uma análise de dados** utilizando Python.

## 🗄️ Competência 02 - Banco de Dados SQL

Três exercícios de consultas SQL envolvendo criação de schemas, inserção de dados e queries complexas.

## 🌐 Competência 03 - Sistema de Gestão com Django

Sistema completo de gerenciamento de empresas, projetos e membros construído com Django 4.2.

### 🎯 Funcionalidades Principais

#### 🔐 Autenticação e Autorização
- Sistema de login/logout
- Três níveis de permissão:
  - **Superusuário**: Gerencia usuários donos de empresas
  - **Dono (staff)**: Cria empresas e gerencia membros/projetos
  - **Membro**: Participa de projetos

#### 🏢 Gestão de Empresas
- Criação de empresas (apenas donos)
- Adicionar/remover membros da empresa
- Visualização de detalhes e projetos vinculados
- Exclusão de empresas (apenas criador)

#### 📁 Gestão de Projetos
- Criação de projetos dentro de empresas
- Adicionar membros de empresas aos projetos
- Restrição: apenas membros da empresa podem participar de seus projetos
- Exclusão de projetos (apenas criador)

#### 👥 Gestão de Usuários (Superusuário)
- CRUD completo de usuários
- Criar "donos de empresas" (usuários staff)
- Edição de perfis e permissões
- Exclusão com confirmação

### 🏗️ Arquitetura

#### Models (`core/models.py`)
```python
Empresa
├── nome: CharField
├── criador: ForeignKey(User)
└── membros: ManyToManyField(User)

Projeto
├── nome: CharField
├── empresa: ForeignKey(Empresa)
├── criador: ForeignKey(User)
└── membros: ManyToManyField(User)
```

#### Views Principais (`core/views.py`)
- `login_view`: Autenticação de usuários
- `dashboard`: Dashboard principal com empresas
- `empresa_view`: Detalhes da empresa e gestão de membros
- `projeto_view`: Detalhes do projeto e gestão de membros
- `usuarios_list`: Gerenciamento de usuários (superuser only)
- CBVs para CRUD completo

#### URLs (`core/urls.py`)
```
/login/                                    # Login
/dashboard/                                # Dashboard
/empresas/<id>/                           # Detalhes empresa
/empresas/criar/                          # Criar empresa
/empresas/<id>/excluir/                   # Excluir empresa
/empresas/<id>/adicionar-membro/          # Adicionar membro
/empresas/<id>/remover-membro/<user_id>/  # Remover membro
/projetos/<id>/                           # Detalhes projeto
/projetos/criar/<empresa_id>/             # Criar projeto
/usuarios/                                # Listar usuários
/usuarios/criar/                          # Criar usuário
```

### 🎨 Frontend

#### Estrutura de Arquivos Estáticos
```
core/static/
├── css/
│   ├── base.css      # Estilos base (navbar, botões, cards, forms)
│   ├── login.css     # Estilos da página de login
│   └── modal.css     # Estilos de modais
└── js/
    └── main.js       # Funções JS (modais, confirmações)
```

#### Design System
- **Cores Principais:** Gradiente roxo/azul (#667eea → #764ba2)
- **Tipografia:** Segoe UI, fonte moderna e legível
- **Componentes:**
  - Cards responsivos com hover effects
  - Modais para adicionar membros
  - Stats cards com bordas coloridas
  - Empty states com ícones SVG
  - Formulários com validação visual

#### Templates Principais
```
templates/
├── login.html                 # Tela de login
├── dashboard.html             # Dashboard principal
├── empresas/
│   ├── empresa.html          # Detalhes da empresa
│   └── criar.html            # Criar empresa
├── projetos/
│   ├── projeto.html          # Detalhes do projeto
│   └── criar.html            # Criar projeto
└── usuarios/
    ├── list.html             # Listar usuários
    ├── create.html           # Criar usuário
    ├── edit.html             # Editar usuário
    └── delete.html           # Confirmar exclusão
```

### 🔒 Sistema de Permissões

#### Hierarquia
```
Superusuário (is_superuser=True)
    ↓ cria
Dono de Empresa (is_staff=True)
    ↓ adiciona como membro
Funcionário (user regular)
    ↓ participa de
Projetos
```

#### Regras de Negócio
1. **Superusuários** podem:
   - Criar usuários "donos" (staff)
   - Acessar painel de gerenciamento de usuários

2. **Donos** podem:
   - Criar empresas
   - Adicionar/remover membros de suas empresas
   - Criar projetos em suas empresas
   - Adicionar membros da empresa aos projetos

3. **Membros** podem:
   - Visualizar empresas e projetos dos quais fazem parte
   - Não podem criar ou modificar estruturas

### 🗃️ Banco de Dados

**SQLite** (desenvolvimento)

**Migrações:**
- `0001_initial.py`: Schema inicial (Empresa e Projeto)
- `0002_empresa_membros.py`: Adiciona campo ManyToMany de membros em Empresa

**Relacionamentos:**
```
User 1──N Empresa (como criador)
User N──N Empresa (como membro)
Empresa 1──N Projeto
User 1──N Projeto (como criador)
User N──N Projeto (como membro)
```

---

## 💻 Tecnologias Utilizadas

### Python & Frameworks
- **Python 3.9+**
- **Django 4.2.26** - Framework web
- **Pandas** - Análise de dados
- **openpyxl** - Manipulação de Excel

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilização (Gradientes, Flexbox, Grid)
- **JavaScript (Vanilla)** - Interatividade

### Banco de Dados
- **SQLite** - Desenvolvimento
- **MySQL** - Exercícios SQL

### Ferramentas
- **Git** - Controle de versão
- **Virtual Environment** - Isolamento de dependências

---

## 🚀 Como Executar

### Pré-requisitos
```bash
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git
```

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/JoaoVitorChaves-05/Akaer.git
cd Akaer
```

### 2️⃣ Criar Ambiente Virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Instalar Dependências
```bash
pip install django pandas openpyxl
```

### 4️⃣ Executar Competência 01 (Algoritmos)
```bash
cd competencia01

# Exercício 01
python 01.py

# Exercício 02
python 02.py

# Exercício 03 (requer DadosLicencas1.xlsx)
python 03.py
```

### 5️⃣ Executar Competência 02 (SQL)
```bash
# Importar no MySQL Workbench ou linha de comando
mysql -u root -p < competencia02/01.SQL
mysql -u root -p < competencia02/02.SQL
mysql -u root -p < competencia02/03.SQL
```

### 6️⃣ Executar Competência 03 (Django)
```bash
cd competencia03

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000/login/`

### 7️⃣ Estrutura de Teste do Sistema Django

#### Primeiro Acesso
1. Faça login com o superusuário criado
2. Acesse "Gerenciar Usuários" no dashboard
3. Crie um usuário "dono" (marque "Staff status")

#### Fluxo Completo
```
1. Login como Superusuário
   ↓
2. Criar usuário dono (João, staff=True)
   ↓
3. Criar usuários que não são donos de empresa (Maria, staff=False)
   ↓
4. Logout e login como João
   ↓
5. Criar empresa "Akaer Engineering"
   ↓
6. Adicionar membros à empresa
   ↓
7. Criar projeto "Sistema ERP"
   ↓
8. Adicionar membros (da empresa) ao projeto
```

---

## 📁 Estrutura do Projeto

```
Akaer/
├── .venv/                          # Ambiente virtual Python
├── competencia01/                  # Algoritmos e Análise de Dados
│   ├── 01.py                      # Número faltante
│   ├── 02.py                      # Pares de botas
│   ├── 03.py                      # Análise de licenças
│   ├── DadosLicencas1.xlsx        # Dados de entrada
│   └── ResultadoLicencas.xlsx     # Resultado gerado
├── competencia02/                  # Banco de Dados SQL
│   ├── 01.SQL                     # Pedidos por cidade
│   ├── 02.SQL                     # Produtos por categoria
│   └── 03.SQL                     # Categoria mais cara
├── competencia03/                  # Sistema Django
│   ├── competencia03/             # Configurações do projeto
│   │   ├── settings.py           # Configurações principais
│   │   ├── urls.py               # URLs raiz
│   │   └── wsgi.py               # WSGI config
│   ├── core/                      # App principal
│   │   ├── migrations/           # Migrações do BD
│   │   ├── static/               # Arquivos estáticos
│   │   │   ├── css/             # Estilos CSS
│   │   │   └── js/              # Scripts JavaScript
│   │   ├── templates/            # Templates HTML
│   │   │   ├── empresas/
│   │   │   ├── projetos/
│   │   │   ├── usuarios/
│   │   │   ├── login.html
│   │   │   └── dashboard.html
│   │   ├── models.py             # Modelos de dados
│   │   ├── views.py              # Views/Controllers
│   │   ├── urls.py               # URLs do app
│   │   └── admin.py              # Admin Django
│   ├── db.sqlite3                 # Banco de dados
│   └── manage.py                  # CLI do Django
└── README.md                       # Este arquivo
```

---

## 🎓 Aprendizados e Desafios

### Competência 01
- **Desafio:** Mesclar intervalos de tempo sobrepostos
- **Solução:** Algoritmo de sweep line ordenando por tempo de início
- **Aprendizado:** Manipulação eficiente de datetime com Pandas

### Competência 02
- **Desafio:** Queries com múltiplos JOINs e agregações
- **Solução:** Utilização de GROUP BY e funções agregadas
- **Aprendizado:** Otimização de queries SQL

### Competência 03
- **Desafio:** Sistema de permissões hierárquico
- **Solução:** Uso de decorators, ForeignKeys e ManyToMany
- **Aprendizado:** 
  - Arquitetura MVC com Django
  - Relacionamentos complexos no ORM
  - Separação de concerns (CSS/JS externos)
  - Sistema de permissões customizado

---

## 👨‍💻 Autor

**João Vitor Mâncio Chaves**

Candidato à vaga de Estágio em Engenharia de Software na **Akaer Engineering**

---

## 📄 Licença

Este projeto foi desenvolvido como parte de um processo seletivo e é de uso exclusivo para avaliação técnica.

---

## 🙏 Agradecimentos

Agradeço à **Akaer Engineering** pela oportunidade de participar deste processo seletivo e demonstrar minhas habilidades técnicas através deste desafio completo e abrangente.

---

<div align="center">
  <strong>Desenvolvido com dedicação para o processo seletivo Akaer 2025</strong>
</div>
