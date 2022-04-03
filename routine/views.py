from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from routine.models import Routine
from routine.serializers import RoutineSerializer


@csrf_exempt
def get_all_routine(request: HttpRequest) -> HttpResponse:
    import json
    r = Routine.objects.first()
    result = RoutineSerializer(r).data
    return HttpResponse(json.dumps(result, default=str))
