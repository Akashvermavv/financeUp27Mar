# Generated by Django 3.0 on 2021-03-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_kycverification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedpackage',
            name='package_start',
            field=models.DateField(),
        ),
    ]
