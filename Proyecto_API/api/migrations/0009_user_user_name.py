# Generated by Django 4.0.2 on 2022-05-15 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_truck_trucktype_user_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
