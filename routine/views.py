from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from routine.models import Routine


@csrf_exempt
def get_all_routine(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        uid = post_data['uid']
        user = User.objects.get(username=uid)
        r = Routine.objects.filter(grade=user.child.grade)
        result = []
        for a in r:
            result.append({
                'day': a.day,
                'first': a.first,
                'second': a.second,
                'third': a.third,
                'fourth': a.fourth,
                'fifth': a.fifth,
                'sixth': a.sixth,
                'seventh': a.seventh,
                'eighth': a.eighth,
            })
        return HttpResponse(json.dumps(result, default=str))
    return HttpResponse('Bad request. Only POST allowed', status=401)
