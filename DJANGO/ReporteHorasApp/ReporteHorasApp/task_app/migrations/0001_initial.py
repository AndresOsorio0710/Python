# Generated by Django 4.0.3 on 2022-08-10 21:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('type', models.CharField(choices=[('PRIORITARY', 'PRIORITARY'), ('INIT', 'INIT'), ('END', 'END')], max_length=10, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['name'],
            },
        ),
    ]
