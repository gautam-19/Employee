# Generated by Django 5.0.6 on 2024-07-11 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_fristname_employee_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='idno',
            new_name='id_no',
        ),
    ]