from django.contrib import admin
from django.db.models import *


# Create your models here.
class AssessmentAdmin(admin.ModelAdmin):
    search_fields = ['task', 'deadline']


class Assessment(Model):
    subject = CharField(max_length=60)
    task = CharField(max_length=255)
    deadline = DateField()
