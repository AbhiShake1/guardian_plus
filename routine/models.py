from django.db.models import *

from child.models import Subject, Grade


class Routine(Model):
    day = CharField(max_length=10, default='Sunday')
    grade = ForeignKey(Grade, on_delete=CASCADE, default=1)
    first = ForeignKey(Subject, on_delete=CASCADE, related_name='first_period')
    second = ForeignKey(Subject, on_delete=CASCADE, related_name='second_period')
    third = ForeignKey(Subject, on_delete=CASCADE, related_name='third_period')
    fourth = ForeignKey(Subject, on_delete=CASCADE, related_name='fourth_period')
    fifth = ForeignKey(Subject, on_delete=CASCADE, related_name='fifth_period')
    sixth = ForeignKey(Subject, on_delete=CASCADE, related_name='sixth_period')
    seventh = ForeignKey(Subject, on_delete=CASCADE, related_name='seventh_period')
    eighth = ForeignKey(Subject, on_delete=CASCADE, related_name='eighth_period')
    ninth = ForeignKey(Subject, on_delete=CASCADE, related_name='ninth_period')

    def __str__(self):
        return str(self.grade)
