# Generated by Django 3.1.3 on 2020-12-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_employee_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='lname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
