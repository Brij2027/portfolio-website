# Generated by Django 3.0.7 on 2020-06-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_name', models.CharField(max_length=50)),
                ('cert_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=30)),
                ('degree_name', models.CharField(max_length=30)),
                ('gpa', models.FloatField()),
                ('date_text', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
    ]