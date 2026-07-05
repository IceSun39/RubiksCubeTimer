import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from .models import Solve, Session, Cube
from pyTwistyScrambler import scrambler333
def index(request):
    current_session = Session.objects.last()
    if not current_session:
        current_session = Session.objects.create()
    session_solves = current_session.solves.all().order_by('-id')

    current_scramble = scrambler333.get_WCA_scramble()

    context = {
        'session': current_session,
        "current_scramble": current_scramble,
        'solves': session_solves,
    }

    return render(request, 'tracker/index.html', context)


@require_POST
def save_solve(request):
    try:
        data = json.loads(request.body)
        time_value = data.get('time')
        scramble_text = data.get('scramble')

        if time_value is None:
            return JsonResponse({'status': 'error', 'message': 'Час не вказано'}, status=400)

        current_session = Session.objects.last()
        if not current_session:
            current_session = Session.objects.create()

        cube = Cube.objects.first()
        if not cube:
            cube = Cube.objects.create(name="Default 3x3", type="regular")

        solve = Solve.objects.create(
            session=current_session,
            cube=cube,
            time=float(time_value),
            scramble=scramble_text
        )

        return JsonResponse({
            'status': 'success',
            'solve_id': solve.id,
            'time': solve.time
        })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)