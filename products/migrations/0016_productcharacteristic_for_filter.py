# Generated by Django 3.2 on 2021-09-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_categorytemplate_for_filter'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcharacteristic',
            name='for_filter',
            field=models.BooleanField(default=False),
        ),
    ]
