from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from routine.models import Routine
from routine.serializers import RoutineSerializer


@csrf_exempt
def get_all_routine(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        grade = post_data['grade']
        r = Routine.objects.get(grade=grade)
        result = RoutineSerializer(r).data
        return HttpResponse(json.dumps(result, default=str))
    return HttpResponse('Bad request. Only POST allowed', status=401)
