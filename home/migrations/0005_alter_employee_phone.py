# Generated by Django 5.0.1 on 2024-07-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_idno_employee_id_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
