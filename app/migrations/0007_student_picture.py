# Generated by Django 3.1.7 on 2021-04-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(null=True, upload_to='students_picture/'),
        ),
    ]
