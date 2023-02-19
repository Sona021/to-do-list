# Generated by Django 4.1.5 on 2023-02-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=45)),
                ('task_description', models.CharField(max_length=100)),
                ('isDone', models.BooleanField()),
            ],
        ),
    ]
