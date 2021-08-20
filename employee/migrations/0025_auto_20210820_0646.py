# Generated by Django 3.1.3 on 2021-08-20 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0024_auto_20210207_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='base_sal',
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('temp', 'Temporary'), ('perm', 'Permanent'), ('mng', 'Managerial')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Start with country code', max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.ForeignKey(help_text='Pick a username', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.worksite', verbose_name='Worksite'),
        ),
    ]
