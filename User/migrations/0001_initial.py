# Generated by Django 2.1 on 2019-04-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiPics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MultiTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('mobile_phone', models.IntegerField()),
                ('profile_pic', models.CharField(max_length=200)),
                ('birth_date', models.DateField(null=True)),
                ('fb_profile', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('donate', models.IntegerField()),
            ],
        ),
    ]
