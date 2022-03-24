# Generated by Django 4.0.3 on 2022-03-24 11:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0006_alter_child_parent_delete_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='current_class',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='progressreport',
            name='term',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]