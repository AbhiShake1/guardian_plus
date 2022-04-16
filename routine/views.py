from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from routine.models import Routine
from routine.serializers import RoutineSerializer


@csrf_exempt
def get_all_routine(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        uid = post_data['uid']
        user = User.objects.get(username=uid)
        r = Routine.objects.get(grade=user.child.grade)
        result = {
            'first': r.first,
            'second': r.second,
            'third': r.third,
            'fourth': r.fourth,
            'fifth': r.fifth,
            'sixth': r.sixth,
            'seventh': r.seventh,
            'eighth': r.eighth,
        }
        return HttpResponse(json.dumps(result, default=str))
    return HttpResponse('Bad request. Only POST allowed', status=401)
