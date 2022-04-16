from django.db.models import *


# Create your models here.
class Feedback(Model):
    title = CharField(max_length=100)
    description = TextField()
