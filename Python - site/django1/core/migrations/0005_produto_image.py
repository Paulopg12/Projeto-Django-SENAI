# Generated by Django 3.2.6 on 2021-09-16 23:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='Image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
