# app/exercises.py
from .utils.tester import run_user_code  # opcional, só pra não dar erro de import

# =========================
# GETTING STARTED – ESTRUTURA CORRETA (lista de dicionários)
# =========================
GETTING_STARTED = [
    {
        "slug": "o-que-e-python",
        "title": "O que é Python?",
        "content": """
            <p>Python é uma linguagem de programação de alto nível, interpretada e muito fácil de aprender.</p>
            <p>Foi criada por Guido van Rossum em 1991 e hoje é uma das mais populares do mundo!</p>
            <p>Usada em: web, ciência de dados, automação, inteligência artificial e muito mais.</p>
        """,
        "has_exercises": False
    },
    {
        "slug": "print",
        "title": "Print e Comentários",
        "content": """
            <p>A função <code>print()</code> exibe texto ou valores na tela:</p>
            <pre><code>print("Olá, mundo!")
print(42, "anos")
# Isso é um comentário</code></pre>
            <p>Comentários começam com <code>#</code> e são ignorados pelo Python.</p>
        """,
        "has_exercises": True,
        "exercises": {
            1: {
                "title": "Hello World",
                "description": "Imprima exatamente: <code>Hello, World!</code>",
                "initial_code": '',
                "test_code": 'assert __output__.strip() == "Hello, World!"'
            },
            2: {
                "title": "Seu nome",
                "description": "Imprima seu primeiro nome",
                "initial_code": 'print("Seu nome aqui")',
                "test_code": 'assert len(__output__.strip()) >= 2'
            },
            3: {
                "title": "Número favorito",
                "description": "Imprima seu número favorito",
                "initial_code": 'print(42)',
                "test_code": 'assert __output__.strip().isdigit()'
            }
        }
    },
    {
        "slug": "variaveis",
        "title": "Variáveis e Tipos",
        "content": """
            <p>Variáveis guardam valores na memória:</p>
            <pre><code>nome = "Maria"
idade = 25
altura = 1.65
ativo = True

print(nome, "tem", idade, "anos")</code></pre>
            <p>Python descobre o tipo automaticamente (int, str, float, bool).</p>
        """,
        "has_exercises": True,
        "exercises": {
            1: {
                "title": "Crie 3 variáveis",
                "description": "Crie variáveis nome, idade e cidade com seus dados",
                "initial_code": 'nome = "Seu nome"\nidade = 20\ncidade = "São Paulo"\nprint(nome, idade, cidade)',
                "test_code": 'assert "nome" in locals() and "idade" in locals()'
            },
            2: {
                "title": "Troque valores",
                "description": "Troque o valor de duas variáveis",
                "initial_code": 'a = 10\nb = 20\n# troque aqui\na, b = b, a\nprint(a, b)',
                "test_code": 'assert __output__.strip() == "20 10"'
            },
            3: {
                "title": "Tipo float",
                "description": "Crie uma variável com sua altura em metros",
                "initial_code": 'altura = 1.75\nprint(type(altura))',
                "test_code": 'assert "float" in __output__'
            }
        }
    }
    # Adicione mais tópicos aqui ↓
]

# Mantém compatibilidade com o sistema antigo (se quiser)
EXERCISES = {
    "getting-started": GETTING_STARTED
    # Se quiser manter os módulos antigos, coloque aqui também
}