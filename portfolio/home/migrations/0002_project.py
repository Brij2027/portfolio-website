# Generated by Django 3.0.7 on 2020-06-18 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_github', models.CharField(max_length=100)),
                ('project_desc', models.TextField()),
            ],
        ),
    ]
