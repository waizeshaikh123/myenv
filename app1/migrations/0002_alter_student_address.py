# Generated by Django 5.0.6 on 2024-05-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
