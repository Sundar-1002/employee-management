# Generated by Django 3.2.5 on 2021-11-20 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=15)),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=15)),
                ('Age', models.CharField(max_length=2)),
            ],
        ),
    ]
