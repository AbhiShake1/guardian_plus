from django.contrib.admin import site
from .models import *

# Register your models here.
site.register(Parent)
site.register(Child)
