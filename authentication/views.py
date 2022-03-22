from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from guardian_plus.settings import RESPONSE_HEADERS
from . import util


@csrf_exempt
def login(request: HttpRequest) -> HttpResponse:
    print(request.user)
    if request.method == 'POST':
        import json
        post_data: dict[str, str] = json.loads(request.body.decode())
        uid: str = post_data['uid']
        password: str = post_data['password']
        user: User = util.login(uid, password)
        if user is None:
            return HttpResponse('Invalid credentials', status=401)
        auth.login(request, user)
        data: dict[str, str] = {
            'uid': uid,
            'is_staff': user.is_staff,
            'is_superuser': user.is_superuser,
        }
        return HttpResponse(json.dumps(data), headers=RESPONSE_HEADERS)
    return HttpResponse('<h2>Bad Request. Only POST allowed</h2>', status=403)


@csrf_exempt
def current_user(request: HttpRequest) -> HttpResponse:
    return HttpResponse(request.user.username)


@csrf_exempt
def signout(request: HttpRequest) -> HttpResponse:
    if request.user is not None:
        auth.logout(request.user)
        return HttpResponse('Successfully logged out')
    return HttpResponse('No user signed in', status=401)
