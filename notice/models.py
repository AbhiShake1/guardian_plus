from django.db.models import *


# Create your models here.
class Notice(Model):
    title = CharField(max_length=255)
    description = TextField()
    startdate = DateField()
    enddate = DateField()

    def __str__(self):
        return f'{self.title} {self.id}'


