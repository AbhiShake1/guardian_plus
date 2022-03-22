from django.db.models import *


# Create your models here.
class Class(Model):
    class_name = CharField(max_length=60)
    class_code = CharField(max_length=8)
