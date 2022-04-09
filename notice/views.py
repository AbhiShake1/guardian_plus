from django.http import HttpRequest, HttpResponse

# Create your views here.
from .models import Notice


def get_all_notices(request: HttpRequest) -> HttpResponse:
    notices: list[dict[str, any]] = []
    import json
    for notice in Notice.objects.all():
        notices.append({
            'title': notice.title,
            'description': notice.description,
            'startDate': notice.startdate,
            'endDate': notice.enddate,
        })
    return HttpResponse(json.dumps(notices, default=str))
