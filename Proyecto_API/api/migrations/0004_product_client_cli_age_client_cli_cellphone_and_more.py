# Generated by Django 4.0.2 on 2022-04-22 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_client_rename_containerid_container_container_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cli_uuid', models.CharField(max_length=64)),
                ('prod_uuid', models.CharField(max_length=64)),
                ('prod_name', models.CharField(max_length=64)),
                ('prod_register_date', models.DateTimeField(auto_now_add=True)),
                ('prod_harvest_date', models.DateTimeField()),
                ('prod_type', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='cli_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='cli_cellphone',
            field=models.CharField(default=str, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='cli_direction',
            field=models.CharField(default=str, max_length=248),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='cli_document',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='client',
            name='cli_document_type',
            field=models.CharField(default=str, max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='cli_email',
            field=models.CharField(default=str, max_length=64),
            preserve_default=False,
        ),
    ]
