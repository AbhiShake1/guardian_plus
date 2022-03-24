# Generated by Django 4.0.3 on 2022-03-24 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current_class', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChildSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parent.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('teaching_hours', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.PositiveIntegerField(default=0)),
                ('marks', models.PositiveIntegerField(default=0)),
                ('student_and_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parent.childsubject')),
            ],
        ),
        migrations.AddField(
            model_name='childsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parent.subject'),
        ),
        migrations.AddField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='parent.parent'),
        ),
    ]
