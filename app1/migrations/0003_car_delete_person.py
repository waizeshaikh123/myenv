# Generated by Django 5.0.6 on 2024-05-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_student_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=500)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]