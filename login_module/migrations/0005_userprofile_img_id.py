# Generated by Django 2.2.5 on 2021-01-29 17:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0004_auto_20210127_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]