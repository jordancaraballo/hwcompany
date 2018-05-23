# Generated by Django 2.0.5 on 2018-05-23 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hwservices', '0002_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('MODEL_NUM', models.AutoField(primary_key=True, serialize=False)),
                ('MODEL_JETS', models.IntegerField(max_length=10)),
                ('MODEL_MOTORS', models.IntegerField(max_length=10)),
                ('MODEL_HP', models.IntegerField(max_length=10)),
                ('MODEL_SRP', models.DecimalField(decimal_places=2, max_digits=8)),
                ('MODEL_HWRP', models.DecimalField(decimal_places=2, max_digits=8)),
                ('MODEL_WEIGTH', models.DecimalField(decimal_places=2, max_digits=8)),
                ('MODEL_WATCAP', models.DecimalField(decimal_places=2, max_digits=8)),
                ('MODEL_SEATCAP', models.IntegerField(max_length=10)),
                ('BRAND_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hwservices.Brand')),
            ],
        ),
    ]
