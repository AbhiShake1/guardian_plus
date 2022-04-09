from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_child_progress(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        user: User = User.objects.get(username=json.loads(request.body.decode())['uid'])
        if user is not None:
            subjects: dict = {}
            for c in user.child.childsubject_set.all():
                pr = c.progressreport
                result = 'Pass' if pr.marks > 39 else 'Fail'
                subjects[str(c.subject)] = {'term': pr.term, 'marks': pr.marks, 'result': result}
            return HttpResponse(json.dumps(subjects, default=str))
        return HttpResponse('No such user found', status=401)
    return HttpResponse('Bad reuqest. Only POST allowed', status=401)
