# Generated by Django 3.2.25 on 2024-05-19 00:08

import Stamp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stamp', '0007_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='patternstamp',
            name='image_example',
            field=models.ImageField(null=True, upload_to=Stamp.models.PatternStamp_image_file_path),
        ),
    ]
