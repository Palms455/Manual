# Generated by Django 3.0.2 on 2020-01-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('termins', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Elements',
            new_name='Element',
        ),
        migrations.RenameModel(
            old_name='Shedule',
            new_name='Schedule',
        ),
        migrations.RenameField(
            model_name='element',
            old_name='shedule',
            new_name='schedule',
        ),
    ]
