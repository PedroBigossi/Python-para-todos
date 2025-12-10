# app/routes.py
import json
from flask import Blueprint, render_template, request, jsonify, url_for, make_response
from .exercises import EXERCISES
from .utils.tester import run_user_code

main = Blueprint('main', __name__)

# =============================================================================
# ROTA PRINCIPAL
# =============================================================================
@main.route('/')
def index():
    return render_template('index.html')


# =============================================================================
# LISTA DE MÓDULOS (grid)
# =============================================================================
@main.route('/modulos')
def modules():
    return render_template('modules.html', modules=EXERCISES.keys())


# =============================================================================
# MÓDULO ANTIGO (opcional, pode apagar se não usa mais)
# =============================================================================
@main.route('/modulo/<module_name>')
def module_detail(module_name):
    if module_name == "getting-started":
        return getting_started()

    if module_name not in EXERCISES:
        return "Módulo não encontrado", 404

    completed_raw = request.cookies.get('completed_exercises', '[]')
    try:
        completed_exercises = json.loads(completed_raw)
    except:
        completed_exercises = []

    return render_template(
        'module/module_detail.html',
        module_name=module_name,
        exercises=EXERCISES[module_name],
        completed_exercises=completed_exercises
    )


# =============================================================================
# GETTING STARTED – SIDEBAR
# =============================================================================
@main.route('/modulo/getting-started')
@main.route('/modulo/getting-started/<topic_slug>')
def getting_started(topic_slug=None):
    topics = EXERCISES["getting-started"]

    if not topic_slug:
        current = topics[0]
    else:
        current = next((t for t in topics if t["slug"] == topic_slug), topics[0])

    return render_template(
        'module/getting_started.html',
        topics=topics,
        current=current,
        topic_slug=current["slug"]
    )


# =============================================================================
# EXERCÍCIO DO GETTING STARTED — 100% CORRIGIDO
# =============================================================================
@main.route('/exercicio/gs/<topic_slug>/<int:ex_id>', methods=['GET', 'POST'])
def gs_exercise(topic_slug, ex_id):
    topics = EXERCISES["getting-started"]
    
    # Encontra o tópico correto pelo slug
    topic = next((t for t in topics if t["slug"] == topic_slug), None)
    if not topic or not topic.get("has_exercises"):
        return "Tópico ou exercício não encontrado", 404

    try:
        exercise = topic["exercises"][ex_id]
    except (KeyError, IndexError):
        return "Exercício não encontrado", 404

    if request.method == 'POST':
        user_code = request.get_json().get('code', '')
        result = run_user_code(user_code, exercise['test_code'])

        if result['success']:
            resp = make_response(jsonify(result))
            # Salva progresso no cookie
            completed_raw = request.cookies.get('completed_exercises', '[]')
            try:
                completed = json.loads(completed_raw)
            except:
                completed = []

            exercise_url = url_for('main.gs_exercise', topic_slug=topic_slug, ex_id=ex_id)
            if exercise_url not in completed:
                completed.append(exercise_url)
                resp.set_cookie('completed_exercises', json.dumps(completed), max_age=60*60*24*365)
            return resp
        else:
            return jsonify(result)

    # GET → mostra o exercício
    return render_template(
        'exercise/exercise_test.html',
        module_name="getting-started",
        topic_slug=topic_slug,
        exercise=exercise,
        ex_id=ex_id
    )