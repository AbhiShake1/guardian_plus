from django.conf.global_settings import AUTH_USER_MODEL
from django.db.models import *
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Subject(Model):
    title = CharField(max_length=255)
    teaching_hours = PositiveIntegerField()

    def __str__(self):
        return self.title


class ChildSubject(Model):
    child_name = ForeignKey('Child', on_delete=CASCADE)
    subject = ForeignKey('Subject', on_delete=CASCADE)

    def __str__(self):
        return f'{self.child_name} {self.subject}'


class Child(Model):
    name = CharField(max_length=255)
    current_class = PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    parent = ForeignKey(AUTH_USER_MODEL, on_delete=CASCADE, default='')

    def __str__(self):
        return f'{self.name} {self.id}'


class ProgressReport(Model):
    student_and_subject = ForeignKey('ChildSubject', on_delete=CASCADE)
    term = PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(4)])
    marks = PositiveIntegerField(default=0)

    def __str__(self):
        return self.student_and_subject
