# Generated by Django 3.2.8 on 2021-11-09 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ashaworkapp', '0013_auto_20211109_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child_module',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
