# Generated by Django 2.1.2 on 2018-11-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20181025_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrofundacion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
