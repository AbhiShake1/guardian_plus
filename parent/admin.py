from django.contrib.admin import site
from .models import *

# Register your models here.
site.register(Child)
site.register(Subject)
site.register(ProgressReport)
site.register(ChildSubject)
