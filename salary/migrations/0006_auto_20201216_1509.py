# Generated by Django 3.1.3 on 2020-12-16 15:09

from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_category_num_of_emp'),
        ('salary', '0005_remove_salary_wages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', month.models.MonthField(null=True)),
                ('remaining_shifts', models.IntegerField(default=0)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'unique_together': {('emp_id', 'month')},
            },
        ),
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', month.models.MonthField(null=True)),
                ('OT_shifts', models.IntegerField(default=0)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('wages', models.FloatField(default=0, null=True)),
                ('claims', models.FloatField(default=0)),
                ('bonus', models.FloatField(default=0)),
                ('OT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salary.overtime')),
                ('deduction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salary.deduction')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
            options={
                'unique_together': {('emp', 'date')},
            },
        ),
        migrations.DeleteModel(
            name='Salary',
        ),
    ]
