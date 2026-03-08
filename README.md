<div align="center">

# Python para Todos

### **Sua plataforma de aprendizado com correção automática e exercícios do zero ao avançado**

<div>

![Static Badge](https://img.shields.io/badge/STATUS%20DO%20PROJETO-Em%20Desenvolvimento-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
<br>

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" width="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-original.svg" width="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="60"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="60"/>

</div>

<br>

**Módulos: Getting Started · Variáveis · Condicionais · Loops · Funções.**  
**100% em português.**

> **Projeto de Extensão — UNIP 2025**  
> Desenvolvido por **Pedro Bigossi**
</div>

---

## O que é o Python para Todos?

Uma **plataforma web open-source** para ensinar Python do zero, com:

- **Editor de código no navegador** (CodeMirror) com syntax highlighting
- **Correção automática** de exercícios (execução segura no backend)
- **Progresso salvo em cookies** (exercícios concluídos no navegador)
- **Layout responsivo** (desktop e celular)
- **Deploy na Vercel** — [python-para-todos.vercel.app](https://python-para-todos.vercel.app/)

---

## Tecnologias

| Tecnologia      | Uso |
|-----------------|-----|
| **Python 3.12**| Backend e lógica da aplicação |
| **Flask**      | Framework web (rotas, blueprints, templates) |
| **Jinja2**     | Templates HTML dinâmicos |
| **Bootstrap 5**| UI responsiva e componentes |
| **CodeMirror** | Editor de código no frontend |
| **Flask-WTF**  | Integração com formulários |
| **ReportLab / Pillow** | (Preparado para geração de certificado em PDF) |
| **python-dotenv** | Variáveis de ambiente em desenvolvimento |
| **Vercel**     | Hospedagem e serverless functions |

---

## Funcionalidades

- **Página inicial** com apresentação do curso
- **Grid de módulos** (`/modulos`) com cards por tema
- **Módulos e lições** com sidebar de navegação (teoria + lista de exercícios)
- **Exercícios interativos** com enunciado, editor de código e botão “Rodar código”
- **Feedback imediato**: saída do programa e resultado do teste (sucesso/erro)
- **Progresso por cookie**: exercícios marcados como concluídos
- **Rotas legadas** com redirect para a estrutura atual (`/exercicio/gs/...`, `/exercicio/<modulo>/<id>`)
- **Tratamento de erros** global (500) para evitar crashes na Vercel

---

## Estrutura do projeto

```
python-para-todos/
├── index.py                 # Entrada da aplicação (Flask app para Vercel)
├── requirements.txt        # Dependências Python
├── .python-version         # Python 3.12 (Vercel / pyenv)
├── .gitignore
├── README.md
│
└── app/
    ├── __init__.py         # create_app(), config (SECRET_KEY, etc.), error handler
    ├── routes.py           # Blueprint principal: /, /modulos, /modulo/..., /exercicio/...
    ├── exercises.py        # Conteúdo dos módulos, lições e exercícios (EXERCISES)
    │
    ├── utils/
    │   └── tester.py       # Execução segura do código do aluno (run_user_code)
    │
    └── templates/
        ├── base.html       # Layout: navbar, Bootstrap 5, estilos
        ├── index.html      # Página inicial
        ├── modules.html    # Grid de módulos
        ├── module/
        │   └── module.html # Página de um módulo/lição (sidebar + conteúdo)
        └── exercise/
            └── exercise_test.html  # Página do exercício (CodeMirror + rodar código)
```

---

## Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/PedroBigossi/Python-para-todos.git
cd Python-para-todos

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Linux/macOS:
# source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. (Opcional) Defina SECRET_KEY no .env ou no ambiente
# No Vercel, configure SECRET_KEY nas variáveis de ambiente do projeto.

# 5. Inicie a aplicação
python index.py
# Ou, com o Flask em modo debug:
# flask --app index run --debug
```

Acesse **http://127.0.0.1:5000**.

---

## Deploy (Vercel)

- O projeto usa **zero-config** para Flask na Vercel: o entrypoint é **`index.py`** (objeto `app`).
- Conecte o repositório ao projeto na Vercel e faça o deploy.
- Em **Settings → Environment Variables**, defina **`SECRET_KEY`** (ex.: `python -c "import secrets; print(secrets.token_hex(32))"`).

---

## Próximos passos (em desenvolvimento)

- Mais exercícios (listas, dicionários, POO)
- Barra de progresso visual por módulo
- Certificado em PDF com nome do aluno (ReportLab)
- Modo escuro

---

## Contribua

Quer ajudar a ensinar Python para mais pessoas?

- Adicionar novos exercícios ou módulos
- Melhorar textos e acessibilidade
- Corrigir bugs ou sugerir melhorias
- Tradução (ex.: inglês, espanhol)

Toda contribuição é bem-vinda.
