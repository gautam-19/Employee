# Generated by Django 5.0.6 on 2024-07-11 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='frist_name',
            new_name='fristname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='id_no',
            new_name='idno',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
