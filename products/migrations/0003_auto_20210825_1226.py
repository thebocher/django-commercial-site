# Generated by Django 3.2 on 2021-08-25 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210825_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='attitude',
            field=models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative')], default='POS', max_length=10),
        ),
    ]