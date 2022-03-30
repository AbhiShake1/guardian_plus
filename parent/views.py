import json

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse

from .models import *


# Create your views here.
def get_children(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        parent: User = request.user
        children: QuerySet = parent.child_set.all()
        return HttpResponse(json.dumps(children, default=str))
    return HttpResponse('No current user found', status=401)


def get_child_subjects(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        import json
        parent: User = User.objects.get(userId=json.loads(request.body.decode())['uid'])
        if parent is not None:
            children: list = parent.child_set.all()
            subjects: dict[str, list[str]] = {}
            for child in children:
                current_child: QuerySet = child.childsubject_set.all()
                cs: ChildSubject
                for c in current_child:
                    if str(c.child_name) in subjects:
                        subjects[str(c.child_name)] += [c.subject]
                    else:
                        subjects[str(c.child_name)] = [c.subject]
            return HttpResponse(json.dumps(subjects, default=str))
        return HttpResponse('No such user found', status=401)
    return HttpResponse('Bad reuqest. Only POST allowed', status=401)
