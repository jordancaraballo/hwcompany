# Generated by Django 2.0.5 on 2018-05-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hwservices', '0003_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='MAN_COMPANY',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='MAN_PHONE',
            field=models.CharField(max_length=8),
        ),
    ]
