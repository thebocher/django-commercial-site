# Generated by Django 3.2 on 2021-09-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20210925_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryfiltervalue',
            name='field_value',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
