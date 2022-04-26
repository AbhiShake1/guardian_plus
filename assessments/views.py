import json

from django.http import HttpRequest, HttpResponse

from .models import Assessment


# Create your views here.
def get_assessments(request: HttpRequest) -> HttpResponse:
    assessments = Assessment.objects.all()
    result: list[dict] = []
    for assessment in assessments:
        result.append({
            'subject': assessment.subject,
            'task': assessment.task,
            'deadline': assessment.deadline,
        })
    return HttpResponse(json.dumps(result, default=str))
