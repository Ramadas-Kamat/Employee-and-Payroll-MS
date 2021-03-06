# Generated by Django 3.1.3 on 2020-12-24 22:37

from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_labourhour'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.category'),
        ),
        migrations.CreateModel(
            name='WorkingShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', month.models.MonthField()),
                ('working_days', models.IntegerField(default=27)),
                ('leaves_allowed', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.category')),
                ('worksite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.worksite')),
            ],
            options={
                'unique_together': {('month', 'worksite', 'category')},
            },
        ),
    ]
