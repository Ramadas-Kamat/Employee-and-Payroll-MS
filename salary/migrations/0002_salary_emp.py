# Generated by Django 3.1.3 on 2020-11-21 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_remove_employee_salary'),
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='emp',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]