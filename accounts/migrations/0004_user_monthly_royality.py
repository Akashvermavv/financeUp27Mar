# Generated by Django 3.0 on 2021-03-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_parent_refer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='monthly_royality',
            field=models.FloatField(default=0.0, max_length=9),
        ),
    ]
