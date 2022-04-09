from django.contrib import admin
from django.db.models import *


# Create your models here.
from child.models import Subject


class AssessmentAdmin(admin.ModelAdmin):
    search_fields = ['task', 'deadline']


class Assessment(Model):
    subject = ForeignKey(Subject, on_delete=CASCADE)
    task = TextField()
    deadline = DateField()

    def __str__(self):
        return f'{self.subject} {self.id}'
