# Generated by Django 4.0.2 on 2022-03-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userid', '0005_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
