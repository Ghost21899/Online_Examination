# Generated by Django 2.2.5 on 2021-01-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0002_auto_20210125_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
    ]