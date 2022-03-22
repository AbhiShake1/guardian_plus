from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from guardian_plus.settings import RESPONSE_HEADERS
from . import util


@csrf_exempt
def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        post_data: dict[str, str] = json.loads(request.body.decode())
        uid: str = post_data['uid']
        password: str = post_data['password']
        user: User = util.login(uid, password)
        if user is None:
            return HttpResponse('Invalid credentials', status=401)
        data: dict[str, str] = {
            'uid': uid,
            'login_date': datetime.now(),
        }
        return HttpResponse(json.dumps(data), headers=RESPONSE_HEADERS)
    return HttpResponse('<h2>Bad Request. Only POST allowed</h2>', status=403)
