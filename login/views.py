from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login page')
