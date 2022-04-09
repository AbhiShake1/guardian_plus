from django.db.models import *


# Create your models here.
class Parent(Model):
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    contactInfo = PositiveIntegerField()

    def __str__(self):
        return f'{self.name} {self.id}'
