# Generated by Django 2.1 on 2019-04-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20190425_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_phone',
            field=models.IntegerField(null=True),
        ),
    ]
