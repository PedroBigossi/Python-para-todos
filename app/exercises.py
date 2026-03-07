# app/exercises.py

def make_lesson(*, slug: str, title: str, content: str = "", exercises: dict[int, dict] | None = None):
    return {
        "slug": slug,
        "title": title,
        "content": content,
        "exercises": exercises or {},
    }


def make_module(*, slug: str, title: str, description: str, lessons: list[dict]):
    return {
        "slug": slug,
        "title": title,
        "description": description,
        "lessons": lessons,
    }


# =============================================================================
# GETTING STARTED (mesmo padrão de módulo)
# =============================================================================
LESSONS_GETTING_STARTED = [
    make_lesson(
        slug="instalando-python",
        title="Instalando Python",
        content="""
            <p>Para instalar o <code>Python</code>, você pode baixar em: </p>
            <ul>
                <li><a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a></li>
                <li><a href="https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=pt-BR&gl=BR" target="_blank">https://apps.microsoft.com/store/detail/python/9P7QFQVHXCLL?hl=pt-br&gl=br</a></li>
            </ul>
            <p>Após a instalação, você pode verificar a versão do Python instalada no terminal com o comando:</p>
            <pre><code>python --version</code></pre>
            <p>Se a versão for exibida, significa que o <code>Python</code> foi instalado corretamente.</p>
            <p>Se não for exibida, significa que o <code>Python</code> não foi instalado corretamente.
            Verifique se o <code>Python</code> está no PATH do sistema.</p>
        """,
    ),
    make_lesson(
        slug="o-que-e-python",
        title="O que é Python?",
        content="""
            <p><strong>Python</strong> é uma linguagem de programação:</p>
            <ul>
              <li><strong>Fácil de ler</strong>: o código parece “quase português/inglês”.</li>
              <li><strong>Interpretada</strong>: você executa e vê o resultado sem precisar “compilar”.</li>
              <li><strong>Multiuso</strong>: serve para sites, automação, dados, IA, scripts e muito mais.</li>
            </ul>

            <p>Quando você escreve Python, você está dando instruções para o computador resolver um problema.
            O objetivo inicial não é “decorar tudo”, e sim entender:</p>
            <ul>
              <li>Como escrever comandos (sintaxe)</li>
              <li>Como guardar valores (variáveis)</li>
              <li>Como tomar decisões (if)</li>
              <li>Como repetir ações (loops)</li>
              <li>Como organizar código (funções)</li>
            </ul>

            <p><strong>Dica</strong>: errar faz parte. Mensagens de erro são “pistas” do que ajustar.</p>
        """,
    ),
    make_lesson(
        slug="como-rodar-python",
        title="Como rodar Python (terminal e arquivos .py)",
        content="""
            <p>Você pode rodar Python de duas formas comuns:</p>
            <ul>
              <li><strong>Interativo</strong>: digitando comandos e vendo o resultado na hora</li>
              <li><strong>Arquivo</strong>: criando um arquivo <code>.py</code> e executando</li>
            </ul>
            <pre><code># no terminal:
python --version
python meu_arquivo.py</code></pre>

            <p>No nosso site, você vai escrever o código e clicar em <strong>Rodar código</strong>.</p>

            <h5>Como ler erros</h5>
            <ul>
              <li><strong>SyntaxError</strong>: erro de “forma” (faltou parêntese, aspas, dois pontos).</li>
              <li><strong>NameError</strong>: você usou um nome que não existe (variável não definida).</li>
              <li><strong>TypeError</strong>: você misturou tipos incompatíveis (ex.: texto + número sem converter).</li>
            </ul>

            <p>Quando aparecer um erro, olhe a última linha: ela costuma dizer o tipo e a causa.</p>
        """,
        exercises={
            1: {
                "title": "Primeiro print",
                "description": "Imprima exatamente: <code>Estou pronto!</code>",
                "test_code": 'assert __output__.strip() == "Estou pronto!"',
            },
            2: {
                "title": "Duas linhas",
                "description": "Imprima duas linhas: <code>Linha 1</code> e <code>Linha 2</code> (uma em cada linha).",
                "test_code": 'assert __output__.splitlines() == ["Linha 1", "Linha 2"]',
            },
            3: {
                "title": "Texto e número",
                "description": "Imprima a frase: <code>Tenho 3 anos de Python</code>",
                "test_code": 'assert __output__.strip() == "Tenho 3 anos de Python"',
            },
        },
    ),
    make_lesson(
        slug="print",
        title="Print e Comentários",
        content="""
            <p>A função <code>print()</code> exibe texto ou valores na tela. É sua principal ferramenta no começo para “ver” o que o programa está fazendo.</p>
            <pre><code>print("Olá, mundo!")
print(42, "anos")
# Isso é um comentário</code></pre>

            <h5>Separador e quebra de linha</h5>
            <p>O <code>print</code> coloca uma quebra de linha no final por padrão. E quando você passa vários valores, ele separa por espaço.</p>
            <pre><code>print("A", "B")       # A B
print("A", "B", sep="-")  # A-B
print("A", end="")   # não quebra linha no final</code></pre>

            <h5>Comentários</h5>
            <p>Comentários começam com <code>#</code>, ajudam a explicar o raciocínio e são ignorados pelo Python.</p>
        """,
        exercises={
            1: {
                "title": "Hello World",
                "description": "Imprima exatamente: <code>Hello, World!</code>",
                "test_code": 'assert __output__.strip() == "Hello, World!"',
            },
            2: {
                "title": "Seu nome",
                "description": "Imprima seu primeiro nome",
                "test_code": 'assert len(__output__.strip()) >= 2',
            },
            3: {
                "title": "Número favorito",
                "description": "Imprima seu número favorito",
                "test_code": 'assert __output__.strip().isdigit()',
            },
        },
    ),
    make_lesson(
        slug="variaveis",
        title="Variáveis e Tipos",
        content="""
            <p><strong>Variáveis</strong> guardam valores na memória para você reutilizar depois. Você cria com <code>=</code> (atribuição).</p>
            <pre><code>nome = "Maria"
idade = 25
altura = 1.65
ativo = True

print(nome, "tem", idade, "anos")</code></pre>

            <h5>Tipos básicos</h5>
            <ul>
              <li><code>int</code>: números inteiros (10, -3, 0)</li>
              <li><code>float</code>: números com decimal (1.5, 3.14)</li>
              <li><code>str</code>: texto ("oi")</li>
              <li><code>bool</code>: verdadeiro/falso (<code>True</code> / <code>False</code>)</li>
            </ul>
            <br>
            <p>Você pode verificar o tipo de uma variável com a função <code>type()</code>.</p>
            <ul>
                <li><code>print(type(10))</code>   # int</li>
                <li><code>print(type(1.5))</code>  # float</li>
                <li><code>print(type("oi"))</code> # str</li>
                <li><code>print(type(True))</code> # bool</li>
            </ul>
            <br>
            <p>Você pode converter o tipo de uma variável com as funções <code>int()</code>, <code>float()</code> e <code>str()</code>.</p>
            <ul>
                <li><code>texto = "42"</code></li>
                <li><code>numero = int(texto)   # 42 (int)</code></li>
                <li><code>altura = float("1.75")</code></li>
            </ul>
            <br>
            <h5>Boas práticas de nomes</h5>
            <ul>
              <li>Use nomes claros: <code>idade_aluno</code>, <code>preco_total</code></li>
              <li>Não use espaços; prefira <code>snake_case</code></li>
              <li>Evite nomes como <code>a</code>, <code>b</code> (só em exemplos curtos)</li>
            </ul>

            <h5>Conversões (muito comum)</h5>
            <pre><code>texto = "42"
numero = int(texto)   # 42 (int)
altura = float("1.75")</code></pre>

            <p><strong>Pegadinha</strong>: <code>"2" + "3"</code> vira <code>"23"</code> (texto). Para somar números, converta para <code>int</code>.</p>
        """,
        exercises={
            1: {
                "title": "Crie 3 variáveis (nomes livres)",
                "description": "Crie <strong>três variáveis</strong> (texto, número inteiro e texto) e imprima as três na mesma linha (separadas por espaço).",
                "test_code": (
                    'parts = __output__.strip().split()\n'
                    "assert len(parts) >= 3\n"
                    'assert parts[1].lstrip("-").isdigit()'
                ),
            },
            2: {
                "title": "Troque valores",
                "description": "Troque o valor de duas variáveis <code>a</code> e <code>b</code>, sendo os valores <code>10</code> e <code>20</code> respectivamente e depois imprima as duas variáveis.",
                "test_code": (
                    'parts = __output__.strip().split()\n'
                    "assert len(parts) == 2\n"
                    'assert parts[0].lstrip("-").isdigit() and parts[1].lstrip("-").isdigit()'
                ),
            },
            3: {
                "title": "Tipo float",
                "description": "Crie uma variável com sua altura em metros e imprima o tipo da variável. <code>dica: use a função type()</code>",
                "test_code": 'assert "float" in __output__',
            },
        },
    ),
    make_lesson(
        slug="operadores",
        title="Operadores e Expressões",
        content="""
            <p>Operadores são símbolos que você usa para fazer contas e comparações.</p>
            <ul>
              <li><code>+</code> soma, <code>-</code> subtração, <code>*</code> multiplicação, <code>/</code> divisão</li>
              <li><code>//</code> divisão inteira, <code>%</code> resto, <code>**</code> potência</li>
            </ul>
            <pre><code>print(10 + 2 * 3)   # 16
print((10 + 2) * 3) # 36</code></pre>

            <h5>Ordem de prioridade</h5>
            <p>Assim como na matemática, multiplicação vem antes de soma. Use parênteses para deixar claro.</p>

            <h5>Divisão</h5>
            <ul>
              <li><code>/</code> sempre gera <code>float</code></li>
              <li><code>//</code> “corta” a parte decimal</li>
              <li><code>%</code> pega o resto (muito usado para par/ímpar)</li>
            </ul>
        """,
        exercises={
            1: {
                "title": "Soma simples",
                "description": "Imprima o resultado de <code>12 + 8</code>.",
                "test_code": 'assert __output__.strip() == "20"',
            },
            2: {
                "title": "Potência",
                "description": "Imprima o resultado de <code>2 ** 5</code>.",
                "test_code": 'assert __output__.strip() == "32"',
            },
            3: {
                "title": "Resto da divisão",
                "description": "Imprima o resto de <code>17 % 5</code>.",
                "test_code": 'assert __output__.strip() == "2"',
            },
        },
    ),
    make_lesson(
        slug="strings",
        title="Strings (texto)",
        content="""
            <p><strong>Strings</strong> são textos entre aspas. Você pode usar aspas duplas ou simples.</p>
            <pre><code>nome = "João"
print(nome.upper())
print(nome[0])</code></pre>

            <h5>Índices</h5>
            <p>Em Python, a contagem começa em 0. Então <code>nome[0]</code> pega o primeiro caractere.</p>

            <h5>Concatenar vs f-string</h5>
            <p>Você pode concatenar com <code>+</code>, mas <strong>f-strings</strong> são mais legíveis:</p>
            <pre><code>idade = 30
print(f"{nome} tem {idade} anos")</code></pre>

            <h5>Funções úteis</h5>
            <pre><code>texto = "  Python  "
print(texto.strip())   # remove espaços nas pontas
print(texto.lower())   # minúsculo
print(texto.upper())   # maiúsculo</code></pre>
        """,
        exercises={
            1: {
                "title": "Maiúsculas",
                "description": "Crie uma string com seu nome e imprima ela em maiúsculas.",
                "test_code": 'assert __output__.strip().isupper() and len(__output__.strip()) >= 2',
            },
            2: {
                "title": "Tamanho do texto",
                "description": "Imprima o tamanho (quantidade de caracteres) da string <code>Python</code> usando <code>len()</code>.",
                "test_code": 'assert __output__.strip() == "6"',
            },
            3: {
                "title": "f-string",
                "description": "Crie as variáveis <code>nome</code> e <code>idade</code> e imprima: <code>&lt;nome&gt; tem &lt;idade&gt; anos</code>.",
                "test_code": 'assert "tem" in __output__ and "anos" in __output__',
            },
        },
    ),
    make_lesson(
        slug="listas",
        title="Listas",
        content="""
            <p><strong>Listas</strong> guardam vários valores em uma única variável. Você cria com <code>[]</code>.</p>
            <pre><code>numeros = [1, 2, 3]
numeros.append(4)
print(numeros)</code></pre>

            <h5>Para que serve</h5>
            <p>Quando você tem “vários itens do mesmo tipo” (notas, nomes, tarefas), uma lista é o jeito mais comum de organizar.</p>

            <h5>Índices</h5>
            <p>Assim como em strings, a lista começa no índice 0: <code>numeros[0]</code> é o primeiro item.</p>

            <h5>Métodos úteis</h5>
            <pre><code>valores = [3, 1, 2]
valores.sort()
print(valores)     # [1, 2, 3]
print(len(valores))</code></pre>
        """,
        exercises={
            1: {
                "title": "Crie uma lista",
                "description": "Crie uma lista com 3 números e imprima a lista.",
                "test_code": 'assert "[" in __output__ and "]" in __output__',
            },
            2: {
                "title": "Acessar índice 0",
                "description": "Crie uma lista com 3 palavras e imprima apenas a primeira (índice 0).",
                "test_code": 'assert len(__output__.strip()) >= 1 and "\\n" in __output__',
            },
            3: {
                "title": "append",
                "description": "Comece com uma lista vazia, adicione dois números com <code>append</code> e imprima a lista.",
                "test_code": 'assert "10" in __output__ and "20" in __output__',
            },
        },
    ),
]


# =============================================================================
# MÓDULOS (estrutura padrão: sempre lessons)
# =============================================================================
EXERCISES_VARIAVEIS = {
    1: {
        "title": "Print com variáveis",
        "description": "Crie duas variáveis (um nome e uma idade) e imprima: <code>Nome: &lt;nome&gt;</code> e <code>Idade: &lt;idade&gt;</code> (cada uma em uma linha).",
        "test_code": (
            'lines = [l.strip() for l in __output__.splitlines() if l.strip()]\n'
            'assert len(lines) == 2\n'
            'assert lines[0].startswith("Nome:")\n'
            'assert lines[1].startswith("Idade:")'
        )
    },
    2: {
        "title": "Conversão para inteiro",
        "description": "Crie uma variável <code>texto</code> com o valor <code>\"42\"</code>, converta para inteiro e imprima o tipo.",
        "test_code": 'assert "int" in __output__'
    },
    3: {
        "title": "Booleano",
        "description": "Crie uma variável booleana e imprima ela (deve aparecer <code>True</code> ou <code>False</code>).",
        "test_code": 'assert __output__.strip() in ("True", "False")'
    },
    4: {
        "title": "Atualize uma variável",
        "description": "Crie <code>x = 5</code>, depois some 3 em <code>x</code> e imprima o resultado.",
        "test_code": 'assert __output__.strip() == "8"'
    },
    5: {
        "title": "Swap sem variável extra",
        "description": "Crie <code>a=1</code> e <code>b=2</code>, troque e imprima <code>a b</code>.",
        "test_code": 'assert __output__.strip() == "2 1"'
    },
    6: {
        "title": "Float e arredondamento",
        "description": "Crie <code>pi = 3.14159</code> e imprima <code>round(pi, 2)</code>.",
        "test_code": 'assert __output__.strip() in ("3.14", "3.15")'
    },
}

EXERCISES_CONDICIONAIS = {
    1: {
        "title": "Maior de idade",
        "description": "Crie <code>idade = 18</code> e imprima <code>Maior</code> se idade >= 18 senão <code>Menor</code>.",
        "test_code": 'assert __output__.strip() in ("Maior", "Menor")'
    },
    2: {
        "title": "Par ou ímpar",
        "description": "Crie <code>n = 7</code> e imprima <code>Par</code> se for par senão <code>Ímpar</code>.",
        "test_code": 'assert __output__.strip() in ("Par", "Ímpar")'
    },
    3: {
        "title": "Nota do aluno",
        "description": "Crie <code>nota = 8</code> e imprima <code>Aprovado</code> se nota >= 7 senão <code>Reprovado</code>.",
        "test_code": 'assert __output__.strip() in ("Aprovado", "Reprovado")'
    },
    4: {
        "title": "Faixa etária (elif)",
        "description": "Crie <code>idade = 12</code>. Imprima <code>Criança</code> (<=12), <code>Adolescente</code> (<=17) ou <code>Adulto</code> (>=18).",
        "test_code": 'assert __output__.strip() in ("Criança", "Adolescente", "Adulto")'
    },
    5: {
        "title": "Operadores lógicos",
        "description": "Crie <code>chuva = True</code> e <code>frio = False</code>. Imprima <code>Casaco</code> se estiver chovendo OU frio, senão <code>Ok</code>.",
        "test_code": 'assert __output__.strip() in ("Casaco", "Ok")'
    },
    6: {
        "title": "Comparações",
        "description": "Crie <code>a=5</code> e <code>b=10</code> e imprima se <code>a &lt; b</code> é verdadeiro.",
        "test_code": 'assert __output__.strip() in ("True", "False")'
    },
}

EXERCISES_LOOPS = {
    1: {
        "title": "For com range",
        "description": "Imprima os números de 1 a 5, um por linha.",
        "test_code": 'assert __output__.splitlines() == ["1","2","3","4","5"]'
    },
    2: {
        "title": "Soma de 1 a 10",
        "description": "Calcule a soma de 1 a 10 usando um loop e imprima o resultado.",
        "test_code": 'assert __output__.strip() == "55"'
    },
    3: {
        "title": "Contar pares",
        "description": "Conte quantos números pares existem de 1 a 10 e imprima a quantidade.",
        "test_code": 'assert __output__.strip() == "5"'
    },
    4: {
        "title": "While (3 repetições)",
        "description": "Use <code>while</code> para imprimir <code>Oi</code> 3 vezes (uma por linha).",
        "test_code": 'assert __output__.splitlines() == ["Oi","Oi","Oi"]'
    },
    5: {
        "title": "Break",
        "description": "Faça um loop de 1 a 10 e pare quando chegar no 4, imprimindo apenas 1,2,3,4 (um por linha).",
        "test_code": 'assert __output__.splitlines() == ["1","2","3","4"]'
    },
    6: {
        "title": "Continue",
        "description": "Imprima de 1 a 5, mas pule o 3 (não imprima o 3).",
        "test_code": 'assert __output__.splitlines() == ["1","2","4","5"]'
    },
}

EXERCISES_FUNCOES = {
    1: {
        "title": "Função simples",
        "description": "Crie uma função <code>saudacao()</code> que imprime <code>Olá!</code> e chame a função.",
        "test_code": 'assert __output__.strip() == "Olá!"'
    },
    2: {
        "title": "Função com parâmetro",
        "description": "Crie <code>ola(nome)</code> que imprime <code>Olá, &lt;nome&gt;!</code> e chame com <code>\"Ana\"</code>.",
        "test_code": 'assert __output__.strip().startswith("Olá,")'
    },
    3: {
        "title": "Retorno",
        "description": "Crie <code>dobro(n)</code> que retorna o dobro e imprima <code>dobro(5)</code>.",
        "test_code": 'assert __output__.strip() == "10"'
    },
    4: {
        "title": "Parâmetro padrão",
        "description": "Crie <code>apresentar(nome, cidade='SP')</code> e imprima uma frase usando os dois valores. Chame com apenas o nome.",
        "test_code": 'assert "mora em" in __output__'
    },
    5: {
        "title": "Escopo básico",
        "description": "Crie uma variável <code>x = 10</code>, uma função que cria <code>x = 5</code> localmente e imprime o x local. Depois imprima o x global.",
        "test_code": 'assert __output__.splitlines() == ["5", "10"]'
    },
    6: {
        "title": "Função que soma",
        "description": "Crie <code>soma(a, b)</code> que retorna a soma. Imprima <code>soma(2, 3)</code>.",
        "test_code": 'assert __output__.strip() == "5"'
    },
}

LESSONS_VARIAVEIS = [
    make_lesson(
        slug="exercicios",
        title="Exercícios",
        content="""
            <p>Neste módulo você pratica <strong>variáveis</strong> e <strong>tipos</strong> (int, float, str, bool).</p>

            <h5>O que você precisa dominar aqui</h5>
            <ul>
              <li><strong>Atribuição</strong>: <code>x = 10</code> (o <code>=</code> não é “igual”, é “recebe”).</li>
              <li><strong>Tipos</strong>: entender quando algo é texto vs número.</li>
              <li><strong>Conversões</strong>: <code>int("10")</code>, <code>float("1.5")</code>, <code>str(123)</code>.</li>
              <li><strong>Saída</strong>: usar <code>print</code> para conferir o que está acontecendo.</li>
            </ul>

            <h5>Erros comuns</h5>
            <ul>
              <li><strong>NameError</strong>: usar variável sem criar primeiro.</li>
              <li><strong>TypeError</strong>: somar texto com número sem converter.</li>
              <li><strong>Confundir vírgula e ponto</strong>: em Python é <code>1.5</code> (ponto), não <code>1,5</code>.</li>
            </ul>
        """,
        exercises=EXERCISES_VARIAVEIS,
    )
]

LESSONS_CONDICIONAIS = [
    make_lesson(
        slug="exercicios",
        title="Exercícios",
        content="""
            <p>Condicionais fazem o programa “tomar decisões”. A base é:</p>
            <pre><code>if condicao:
    # roda se for True
elif outra_condicao:
    # roda se a primeira for False e esta for True
else:
    # roda se nenhuma condição for True</code></pre>

            <h5>Comparações mais usadas</h5>
            <ul>
              <li><code>==</code> igual, <code>!=</code> diferente</li>
              <li><code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code></li>
              <li><code>and</code>, <code>or</code>, <code>not</code></li>
            </ul>

            <h5>Erros comuns</h5>
            <ul>
              <li>Esquecer os <code>:</code> após o <code>if</code>/<code>elif</code>/<code>else</code></li>
              <li>Indentação errada (o bloco precisa estar “tabulado”)</li>
              <li>Confundir <code>=</code> (atribuição) com <code>==</code> (comparação)</li>
            </ul>
        """,
        exercises=EXERCISES_CONDICIONAIS,
    )
]

LESSONS_LOOPS = [
    make_lesson(
        slug="exercicios",
        title="Exercícios",
        content="""
            <p>Loops servem para repetir ações sem copiar e colar código.</p>

            <h5><code>for</code> com <code>range</code></h5>
            <pre><code>for i in range(5):
    print(i)  # 0,1,2,3,4</code></pre>
            <p>Se você quer de 1 a 5, use <code>range(1, 6)</code> (o final não entra).</p>

            <h5><code>while</code></h5>
            <pre><code>i = 0
while i &lt; 3:
    print(i)
    i += 1</code></pre>

            <h5><code>break</code> e <code>continue</code></h5>
            <ul>
              <li><code>break</code> sai do loop</li>
              <li><code>continue</code> pula para a próxima repetição</li>
            </ul>

            <h5>Erros comuns</h5>
            <ul>
              <li><strong>Loop infinito</strong> no <code>while</code> (esquecer de atualizar a variável)</li>
              <li>Confundir a contagem do <code>range</code></li>
            </ul>
        """,
        exercises=EXERCISES_LOOPS,
    )
]

LESSONS_FUNCOES = [
    make_lesson(
        slug="exercicios",
        title="Exercícios",
        content="""
            <p>Funções ajudam a <strong>organizar</strong> o código e evitar repetição.</p>

            <h5>Definindo uma função</h5>
            <pre><code>def saudacao():
    print("Olá!")</code></pre>

            <h5>Parâmetros e retorno</h5>
            <pre><code>def dobro(n):
    return n * 2

resultado = dobro(5)  # 10</code></pre>

            <h5>Quando usar função?</h5>
            <ul>
              <li>Quando você precisa repetir a mesma lógica em vários lugares</li>
              <li>Quando um trecho está grande e você quer dar um nome para ele</li>
            </ul>

            <h5>Erros comuns</h5>
            <ul>
              <li>Esquecer de chamar a função (só criar não executa)</li>
              <li>Esquecer <code>return</code> quando precisa do valor de volta</li>
            </ul>
        """,
        exercises=EXERCISES_FUNCOES,
    )
]


# Catálogo dos módulos exibidos na tela /modulos
EXERCISES = {
    "getting-started": make_module(
        slug="getting-started",
        title="Getting Started",
        description="Primeiros passos com Python: como rodar código, print, variáveis, operadores, strings e listas.",
        lessons=LESSONS_GETTING_STARTED,
    ),
    "variaveis": make_module(
        slug="variaveis",
        title="Variáveis e Tipos",
        description="Tipos básicos, conversões e boas práticas de variáveis.",
        lessons=LESSONS_VARIAVEIS,
    ),
    "condicionais": make_module(
        slug="condicionais",
        title="Condicionais",
        description="if/elif/else, operadores lógicos e comparações.",
        lessons=LESSONS_CONDICIONAIS,
    ),
    "loops": make_module(
        slug="loops",
        title="Laços (Loops)",
        description="for, while, range, break e continue.",
        lessons=LESSONS_LOOPS,
    ),
    "funcoes": make_module(
        slug="funcoes",
        title="Funções",
        description="def, parâmetros, retorno e escopo básico.",
        lessons=LESSONS_FUNCOES,
    ),
}