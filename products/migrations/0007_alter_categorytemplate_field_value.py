# Generated by Django 3.2 on 2021-08-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_categorytemplate_field_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytemplate',
            name='field_value',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
