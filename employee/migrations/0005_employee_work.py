# Generated by Django 3.1.3 on 2020-11-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20201116_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.worksite'),
        ),
    ]
