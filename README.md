<<<<<<< HEAD

# **Sistema de Comércio de Automóveis**

Este é um sistema completo para gestão de vendas de automóveis, desenvolvido com **Django** (backend), **React** (frontend) e **PostgreSQL** (banco de dados). O projeto foi dockerizado para facilitar a execução.

## **Requisitos do Sistema**
Antes de começar, certifique-se de ter instalado:
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+](https://nodejs.org/)
- [Docker e Docker Compose](https://docs.docker.com/get-docker/)

---

## **Passo a Passo de Instalação**

### **1. Clonando o Repositório**
Clone este repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/sistema-comercio-automoveis.git
cd sistema-comercio-automoveis
```

---

### **2. Configuração do Backend**

1. Acesse a pasta do backend:
   ```bash
   cd backend
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows
   ```

3. Instale as dependências do backend:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados PostgreSQL em `backend/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'comercio_db',
           'USER': 'postgres',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Execute as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Inicie o servidor backend:
   ```bash
   python manage.py runserver
   ```

O backend estará disponível em: **http://127.0.0.1:8000**

---

### **3. Configuração do Frontend**

1. Acesse a pasta do frontend:
   ```bash
   cd ../frontend
   ```

2. Instale as dependências do frontend:
   ```bash
   npm install
   ```

3. Inicie o servidor do React:
   ```bash
   npm start
   ```

O frontend estará disponível em: **http://localhost:3000**

---

### **4. Executando com Docker**

Caso prefira usar Docker para gerenciar os serviços:

1. Certifique-se de que o Docker e o Docker Compose estão instalados na sua máquina.
2. Execute o comando na raiz do projeto:
   ```bash
   docker-compose up --build
   ```

Os serviços estarão disponíveis em:
- Backend: **http://localhost:8000**
- Frontend: **http://localhost:3000**

---

## **Estrutura do Projeto**

```
sistema-comercio-automoveis/
├── backend/       # Código do backend (Django)
├── frontend/      # Código do frontend (React)
├── docker/        # Configurações do Docker
└── README.md      # Documentação do projeto
```

---

## **Funcionalidades do Sistema**

- **Cadastro de Clientes**: Nome, CPF, telefone e e-mail.
- **Cadastro de Automóveis**: Marca, modelo, ano, valor e status (disponível/vendido).
- **Gestão de Vendas**: Registro de vendas associando cliente e automóvel.
- **API REST**: Endpoints para gerenciamento dos dados.
- **Interface Responsiva**: Visualização de automóveis disponíveis.

---

## **Contribuição**
Se quiser contribuir para o projeto:
1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Envie um pull request com suas alterações.


=======
# projeto-integrado-comercio-automoveis
>>>>>>> 087d7093ab1c877e839b2b61b060c07b3d784267
