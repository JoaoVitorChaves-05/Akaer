# 🚀 Teste Técnico - Akaer Engenharia - Estágio

Repositório contendo as soluções para o processo seletivo de estágio na **Akaer Engenharia**. O teste está dividido em quatro competências que avaliam diferentes habilidades técnicas essenciais para a vaga.

## 📝 Resumo Executivo

Este projeto demonstra competências em:
- **Algoritmos e Estruturas de Dados**: Resolução de problemas computacionais com Python
- **Banco de Dados SQL**: Queries complexas com JOINs, agregações e funções
- **Desenvolvimento Web Full-Stack**: Sistema completo em Django com autenticação, autorização e CRUD
- **Análise de Dados**: Manipulação de dados com Pandas e Excel

**Destaques Técnicos:**
- ✅ Modelo de usuário customizado sem coluna `id` (username como PK)
- ✅ Sistema de permissões hierárquico (3 níveis)
- ✅ Tratamento robusto de erros e validações
- ✅ Separação de concerns (CSS/JS externos)
- ✅ Interface responsiva e intuitiva

---

## 📋 Índice

- [Competência 01 - Algoritmos e Análise de Dados](#-competência-01---algoritmos-e-análise-de-dados)
- [Competência 02 - Banco de Dados SQL](#-competência-02---banco-de-dados-sql)
- [Competência 03 - Sistema de Gestão com Django](#-competência-03---sistema-de-gestão-com-django)
- [Competência 04 - Teste de Excel](#-competência-04---teste-de-excel)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)

---

## 📚 Competência 01 - Algoritmos e Análise de Dados

Nesta competência foram resolvidos **dois desafios de programação** (judges) e **uma análise de dados** utilizando Python e Pandas.

---

## 🗄️ Competência 02 - Banco de Dados SQL

Três exercícios de consultas SQL envolvendo criação de schemas, inserção de dados e queries complexas com JOINs e agregações.

---

## 🌐 Competência 03 - Sistema de Gestão com Django

Sistema completo de gerenciamento de empresas, projetos e membros construído com Django 4.2, incluindo autenticação, autorização hierárquica e modelo de usuário customizado.

---

## 📊 Competência 04 - Teste de Excel

Exercícios práticos de Excel envolvendo manipulação de dados, fórmulas e formatação. O arquivo `Teste (Excel) - Resolvido.xlsx` contém as soluções implementadas.

---

### 🎯 Funcionalidades Principais

#### 🔐 Autenticação e Autorização
- Sistema de login/logout com sessões
- Três níveis hierárquicos de permissão:
  - **Superusuário** (`is_superuser=True`): Administra usuários donos de empresas
  - **Dono de Empresa** (`is_staff=True`): Cria empresas e gerencia membros/projetos
  - **Membro**: Participa de projetos e visualiza informações da empresa

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
- Username como identificador único (não editável após criação)
- Tratamento de erros de integridade (username duplicado)
- Exclusão com confirmação

### 🏗️ Arquitetura

#### Models (`core/models.py`)
```python
CustomUser (username como PRIMARY KEY, sem coluna id)
├── username: CharField(primary_key=True)
├── email: EmailField
├── first_name: CharField
├── last_name: CharField
├── is_active: BooleanField
├── is_staff: BooleanField
└── date_joined: DateTimeField

Empresa
├── nome: CharField
├── criador: ForeignKey(CustomUser)
└── membros: ManyToManyField(CustomUser)

Projeto
├── nome: CharField
├── empresa: ForeignKey(Empresa)
├── criador: ForeignKey(CustomUser)
└── membros: ManyToManyField(CustomUser)
```

#### Views Principais (`core/views.py`)
- `login_view`: Autenticação de usuários e controle de sessão
- `logout_view`: Encerramento de sessão
- `dashboard`: Dashboard principal listando empresas (filtradas por permissão)
- `empresa_view`: Detalhes da empresa e gestão de membros/projetos
- `projeto_view`: Detalhes do projeto e gestão de membros
- `usuarios_list`: Listagem de usuários (superuser only)
- `usuario_create`: Criação de usuários com tratamento de IntegrityError
- `usuario_edit`: Edição de usuários (username readonly)
- `usuario_delete`: Exclusão de usuários com confirmação
- CBVs (CreateView, DeleteView) para CRUD de empresas e projetos

#### URLs (`core/urls.py`)
```
/login/                                         # Login
/logout/                                        # Logout
/                                               # Dashboard
/empresas/criar/                                # Criar empresa
/empresas/<id>/                                 # Detalhes empresa
/empresas/<id>/delete/                          # Excluir empresa
/empresas/<empresa_id>/adicionar-membro/        # Adicionar membro à empresa
/empresas/<empresa_id>/remover-membro/<user_id>/  # Remover membro da empresa
/empresas/<empresa_id>/projetos/criar/          # Criar projeto
/projetos/<id>/                                 # Detalhes projeto
/projetos/<id>/delete/                          # Excluir projeto
/projetos/<id_projeto>/adicionar-membro/        # Adicionar membro ao projeto
/projetos/<id_projeto>/remover-membro/<id_usuario>/  # Remover membro do projeto
/usuarios/                                      # Listar usuários (superuser)
/usuarios/criar/                                # Criar usuário (superuser)
/usuarios/<username>/editar/                    # Editar usuário (superuser)
/usuarios/<username>/deletar/                   # Deletar usuário (superuser)
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
   - Criar empresas (apenas se `is_staff=True`)
   - Adicionar/remover membros de suas empresas
   - Criar projetos em suas empresas
   - Adicionar membros da empresa aos projetos
   - Visualizar TODOS os projetos da empresa (não apenas os criados por ele)

3. **Membros** podem:
   - Visualizar empresas e projetos dos quais fazem parte
   - Não podem criar ou modificar estruturas

#### Validações e Restrições
- **Username único**: Sistema impede criação de usernames duplicados com mensagem de erro
- **Username imutável**: Após criação, o username não pode ser alterado (campo readonly)
- **Uma empresa por usuário**: Cada usuário pode pertencer a apenas uma empresa
- **Membros de projeto**: Apenas membros da empresa podem ser adicionados aos projetos
- **Exclusão**: Apenas o criador pode excluir empresas e projetos

### 🗃️ Banco de Dados

**SQLite** (desenvolvimento)

**Modelo de Usuário Customizado:**
- Implementado `CustomUser` com `username` como PRIMARY KEY
- **Não possui coluna `id`** (conforme requisito do exercício)
- Gerenciado por `CustomUserManager` para criação de usuários e superusuários
- Configurado em settings.py: `AUTH_USER_MODEL = 'core.CustomUser'`

**Migrações:**
- `0001_initial.py`: Schema inicial com CustomUser, Empresa e Projeto

**Relacionamentos:**
```
CustomUser 1──N Empresa (como criador)
CustomUser N──N Empresa (como membro)
Empresa 1──N Projeto
CustomUser 1──N Projeto (como criador)
CustomUser N──N Projeto (como membro)
```

---

## 💻 Tecnologias Utilizadas

### Backend
- **Python 3.9+** - Linguagem principal
- **Django 4.2.26** - Framework web full-stack
- **SQLite** - Banco de dados (desenvolvimento)

### Análise de Dados
- **Pandas** - Manipulação e análise de dados
- **openpyxl** - Leitura/escrita de arquivos Excel

### Frontend
- **HTML5** - Estrutura
- **CSS3** - Estilização (Gradientes, Flexbox, Grid)
- **JavaScript (Vanilla)** - Interatividade

### Banco de Dados
- **SQLite** - Banco embarcado (Django)
- **MySQL** - Exercícios SQL da competência 02

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

# Exercício 01 - Número faltante
python 01.py

# Exercício 02 - Pares de botas
python 02.py

# Exercício 03 - Análise de licenças (requer DadosLicencas1.xlsx)
python 03.py
```

### 5️⃣ Executar Competência 02 (SQL)
```bash
# Importar no MySQL Workbench ou linha de comando
mysql -u root -p < competencia02/01.SQL
mysql -u root -p < competencia02/02.SQL
mysql -u root -p < competencia02/03.SQL
```

### 7️⃣ Executar Competência 03 (Django)
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

### 8️⃣ Visualizar Competência 04 (Excel)
```bash
# Abrir o arquivo Excel com as soluções
# competencia04/Teste (Excel) - Resolvido.xlsx
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
├── competencia04/                  # Teste de Excel
│   └── Teste (Excel) - Resolvido.xlsx  # Exercícios resolvidos
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

## ✨ Destaques Técnicos

### Modelo de Usuário Customizado
- Implementação de `CustomUser` com **username como PRIMARY KEY**
- Ausência da coluna `id` conforme requisito do exercício
- `CustomUserManager` para gerenciamento de criação de usuários
- Tratamento robusto de erros de integridade (username duplicado)

### Sistema de Permissões
- **Arquitetura hierárquica** com três níveis de acesso
- Controle granular de operações (CRUD) por perfil
- Validações no backend e frontend

### Boas Práticas
- **Separação de concerns**: CSS e JS externalizados
- **DRY Principle**: Reutilização de templates e estilos
- **Segurança**: Proteção contra edição de chave primária
- **UX**: Mensagens de erro claras e formulários validados

---

## 🎓 Aprendizados e Desafios

### Competência 01
- **Desafio:** Mesclar intervalos de tempo sobrepostos
- **Solução:** Algoritmo de sweep line ordenando por tempo de início
- **Aprendizado:** Manipulação eficiente de datetime com Pandas

### Competência 02
- **Desafio:** Queries com múltiplos JOINs e agregações
- **Solução:** Utilização de GROUP BY e funções agregadas (SUM, AVG, MAX)
- **Aprendizado:** Otimização de queries SQL e normalização de dados

### Competência 03
- **Desafio:** Sistema de permissões hierárquico com modelo de usuário customizado
- **Solução:** Uso de decorators, ForeignKeys, ManyToMany e CustomUser sem coluna ID
- **Aprendizado:** 
  - Arquitetura MVC com Django
  - Relacionamentos complexos no ORM
  - Separação de concerns (CSS/JS externos)
  - Sistema de permissões customizado
  - Modelo de usuário customizado com username como PK
  - Tratamento de erros de integridade no banco

### Competência 04
- **Desafio:** Manipulação e análise de dados em Excel
- **Solução:** Aplicação de fórmulas, formatação condicional e organização de dados
- **Aprendizado:** Proficiência em Excel para análise de dados

---

## 👨‍💻 Autor

**João Vitor Mâncio Chaves**

Candidato à vaga de Estágio em Análise de Dados na **Akaer Engenharia**

📧 Contato disponível no perfil do GitHub

---

## 📄 Licença

Este projeto foi desenvolvido como parte de um processo seletivo e é de uso exclusivo para avaliação técnica.

---

## 🙏 Agradecimentos

Agradeço à **Akaer Engenharia** pela oportunidade de participar deste processo seletivo e demonstrar minhas habilidades técnicas através deste desafio completo e abrangente.

---

<div align="center">
  <strong>Desenvolvido com dedicação para o processo seletivo Akaer 2025</strong>
</div>
