# Generated by Django 3.1.4 on 2021-02-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('birthday', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('social_url', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
