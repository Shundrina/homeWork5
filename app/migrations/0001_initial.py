# Generated by Django 3.1.7 on 2021-03-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('birthday', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('social_url', models.CharField(max_length=200, null=True)),
                ('normalized_name', models.CharField(max_length=200,
                                                     null=True)),
                ('book', models.OneToOneField(
                    null=True, on_delete=django.db.models.deletion.CASCADE,
                    related_name='student', related_query_name='student',
                    to='app.book')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('students', models.ManyToManyField(
                    related_name='teachers', related_query_name='teachers',
                    to='app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL,
                related_name='students', related_query_name='students',
                to='app.subject'),
        ),
    ]
