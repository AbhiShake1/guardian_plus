# Generated by Django 4.0.3 on 2022-04-09 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0002_childsubject_progressreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progressreport',
            name='student_and_subject',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='child.childsubject'),
        ),
    ]
