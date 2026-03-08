# app/routes.py
import json
from flask import Blueprint, render_template, request, jsonify, url_for, make_response, redirect
from .exercises import EXERCISES
from .utils.tester import run_user_code

main = Blueprint('main', __name__)

def _load_completed_exercises():
    completed_raw = request.cookies.get("completed_exercises", "[]")
    try:
        completed = json.loads(completed_raw)
        if isinstance(completed, list):
            return completed
        return []
    except Exception:
        return []


def _mark_completed(resp, exercise_url: str):
    completed = _load_completed_exercises()
    if exercise_url not in completed:
        completed.append(exercise_url)
        resp.set_cookie("completed_exercises", json.dumps(completed), max_age=60 * 60 * 24 * 365)
    return resp


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
    module_cards = []
    for slug, module in EXERCISES.items():
        lessons = module.get("lessons", [])
        count = sum(len(lesson.get("exercises", {})) for lesson in lessons)

        module_cards.append(
            {
                "slug": slug,
                "title": module.get("title", slug),
                "description": module.get("description", ""),
                "exercise_count": count,
            }
        )

    return render_template('modules.html', modules=module_cards)


# =============================================================================
# MÓDULO (um padrão só)
# =============================================================================
@main.route('/modulo/<module_slug>')
@main.route('/modulo/<module_slug>/<lesson_slug>')
def module_view(module_slug, lesson_slug=None):
    module = EXERCISES.get(module_slug)
    if not module:
        return "Módulo não encontrado", 404

    lessons = module.get("lessons", [])
    if not lessons:
        return "Módulo sem lições", 404

    if not lesson_slug:
        current = lessons[0]
    else:
        current = next((l for l in lessons if l.get("slug") == lesson_slug), lessons[0])

    return render_template(
        'module/module.html',
        module=module,
        lessons=lessons,
        current=current,
        lesson_slug=current["slug"],
        completed_exercises=_load_completed_exercises(),
    )


# =============================================================================
# EXERCÍCIO (um padrão só)
# =============================================================================
@main.route('/exercicio/<module_slug>/<lesson_slug>/<int:ex_id>', methods=['GET', 'POST'])
def exercise(module_slug, lesson_slug, ex_id):
    module = EXERCISES.get(module_slug)
    if not module:
        return "Módulo não encontrado", 404

    lesson = next((l for l in module.get("lessons", []) if l.get("slug") == lesson_slug), None)
    if not lesson:
        return "Lição não encontrada", 404

    exercises = lesson.get("exercises", {})
    if ex_id not in exercises:
        return "Exercício não encontrado", 404

    exercise_data = exercises[ex_id]

    if request.method == 'POST':
        payload = request.get_json(silent=True) or {}
        user_code = payload.get('code', '')
        result = run_user_code(user_code, exercise_data['test_code'])

        if result['success']:
            resp = make_response(jsonify(result))
            exercise_url = url_for('main.exercise', module_slug=module_slug, lesson_slug=lesson_slug, ex_id=ex_id)
            return _mark_completed(resp, exercise_url)

        return jsonify(result)

    return render_template(
        'exercise/exercise_test.html',
        module_name=module_slug,
        back_url=url_for('main.module_view', module_slug=module_slug, lesson_slug=lesson_slug),
        back_label="Voltar para a lição",
        exercise=exercise_data,
        ex_id=ex_id
    )


# =============================================================================
# Rotas antigas (compatibilidade)
# =============================================================================
@main.route('/exercicio/gs/<topic_slug>/<int:ex_id>')
def legacy_gs_exercise(topic_slug, ex_id):
    return redirect(url_for("main.exercise", module_slug="getting-started", lesson_slug=topic_slug, ex_id=ex_id))


@main.route('/exercicio/<module_name>/<int:ex_id>')
def legacy_module_exercise(module_name, ex_id):
    return redirect(url_for("main.exercise", module_slug=module_name, lesson_slug="exercicios", ex_id=ex_id))