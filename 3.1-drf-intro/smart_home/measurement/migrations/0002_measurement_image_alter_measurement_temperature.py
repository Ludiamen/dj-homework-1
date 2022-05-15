# Generated by Django 4.0.4 on 2022-05-15 18:21

from django.db import migrations, models
import measurement.models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=measurement.models.image_path),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
