from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import *

from parent.models import Parent


class Subject(Model):
    title = CharField(max_length=255)
    teaching_hours = PositiveIntegerField()

    def __str__(self):
        return self.title


class Grade(Model):
    grade = PositiveIntegerField(default=1)
    section = CharField(max_length=1)

    def __str__(self):
        return f'{self.grade} {self.section}'


class Child(Model):
    child = OneToOneField(User, on_delete=CASCADE, default='not set')
    parent = ForeignKey(Parent, on_delete=CASCADE, default='not set')
    imageUrl = TextField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460__480.png')
    school = CharField(max_length=200, default='')
    grade = ForeignKey(Grade, on_delete=CASCADE, default=1)

    def __str__(self):
        return f'{self.child.username} {self.id}'


class ChildSubject(Model):
    child = ForeignKey(Child, on_delete=CASCADE)
    subject = ForeignKey(Subject, on_delete=CASCADE)

    def __str__(self):
        return f'{self.child} {self.subject}'


class ProgressReport(Model):
    student_and_subject = OneToOneField(ChildSubject, on_delete=CASCADE)
    term = PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(4)])
    marks = PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return str(self.student_and_subject)
