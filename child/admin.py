from django.contrib.admin import *
from .models import *

# Register your models here.
site.register(Child)
site.register(Subject)
site.register(Grade)
site.register(ChildSubject)
site.register(ProgressReport)
