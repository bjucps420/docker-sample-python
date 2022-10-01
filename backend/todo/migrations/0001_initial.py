# Generated by Django 4.1.1 on 2022-09-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
