from django.db.models import *


# Create your models here.
class Child(Model):
    name = CharField(max_length=255)
    current_class = PositiveIntegerField()
    parent = ForeignKey('Parent', on_delete=CASCADE)

    def __str__(self):
        return self.name


class Parent(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name
