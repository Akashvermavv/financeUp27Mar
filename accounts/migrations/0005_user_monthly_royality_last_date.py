# Generated by Django 3.0 on 2021-03-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_monthly_royality'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='monthly_royality_last_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
