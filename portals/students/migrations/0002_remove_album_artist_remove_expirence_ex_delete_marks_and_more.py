# Generated by Django 4.1.7 on 2023-06-18 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='expirence',
            name='ex',
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='expirence',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
    ]
