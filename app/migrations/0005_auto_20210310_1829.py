# Generated by Django 3.1.7 on 2021-03-10 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210307_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='students', to='app.subject'),
        ),
    ]
