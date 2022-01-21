# Generated by Django 3.1.2 on 2022-01-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
