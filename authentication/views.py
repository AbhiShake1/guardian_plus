from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from guardian_plus.settings import RESPONSE_HEADERS
from . import util


@csrf_exempt
def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        uid: str = str(request.POST['uid'])
        password: str = str(request.POST['password'])
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
    return HttpResponse(request.user.username, headers=RESPONSE_HEADERS)


@csrf_exempt
def signout(request: HttpRequest) -> HttpResponse:
    if request.user is not None:
        auth.logout(request.user)
        return HttpResponse('Successfully logged out', headers=RESPONSE_HEADERS)
    return HttpResponse('No user signed in', status=401)


@csrf_exempt
def update_password(request: HttpRequest) -> HttpResponse:
    if request.method == 'PUT':
        if request.user is not None:
            import json
            post_data = json.loads(request.body.decode())
            request.user.set_password(post_data['password'])
            return HttpResponse('Successfully updated', headers=RESPONSE_HEADERS)
        return HttpResponse('No user signed in', status=401)
    return HttpResponse('<h2>Wrong request. Only PUT allowed</h2>', status=403)
