# Generated by Django 3.1.4 on 2021-02-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='normalized_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]