# Generated by Django 3.0 on 2021-03-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210316_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='kycverification',
            name='other_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
