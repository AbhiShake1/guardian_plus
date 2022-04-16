from django.http import HttpResponse

# Create your views here.
from feedback.models import Feedback


def post_feedback(request):
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode())
        title = post_data['title']
        description = post_data['description']
        Feedback.objects.create(title=title, description=description)
    return HttpResponse('Only POST allowed', status=401)
