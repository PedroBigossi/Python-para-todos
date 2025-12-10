# app/utils/tester.py
import sys
from io import StringIO
import contextlib

# Funções e objetos seguros que o aluno pode usar
SAFE_BUILTINS = {
    '__import__': __import__,
    'abs': abs,
    'all': all,
    'any': any,
    'bool': bool,
    'chr': chr,
    'divmod': divmod,
    'enumerate': enumerate,
    'float': float,
    'int': int,
    'len': len,
    'list': list,
    'max': max,
    'min': min,
    'ord': ord,
    'pow': pow,
    'print': print,
    'range': range,
    'reversed': reversed,
    'round': round,
    'sorted': sorted,
    'str': str,
    'sum': sum,
    'tuple': tuple,
    'type': type,
    'zip': zip,
    'locals': locals,      # ← necessário para exercícios com variáveis
    'globals': globals,    # ← bom ter
    'dict': dict,
    'set': set,
    'frozenset': frozenset,
}

@contextlib.contextmanager
def capture_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield new_out
    finally:
        sys.stdout = old_out

def run_user_code(user_code: str, test_code: str):
    output = ""
    try:
        with capture_output() as out:
            # Executa o código do aluno
            exec(user_code, {"__builtins__": SAFE_BUILTINS})

        output = out.getvalue()

        # Passa variáveis úteis pro teste
        test_locals = {
            "__output__": output,
        }

        # Executa o teste (também com built-ins seguros)
        exec(test_code, {"__builtins__": SAFE_BUILTINS}, test_locals)

        return {"success": True, "output": output}

    except AssertionError:
        return {"success": False, "output": output, "error": "Teste falhou"}
    except Exception as e:
        return {"success": False, "output": output, "error": str(e)}