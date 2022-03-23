import json

from django.http import HttpRequest, HttpResponse

from .models import Assessment


# Create your views here.
def get_assessments(request: HttpRequest) -> HttpResponse:
    assessments = list(Assessment.objects.all().values())
    return HttpResponse(json.dumps(assessments, indent=4, sort_keys=True, default=str))
