# Generated by Django 3.2.4 on 2021-06-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('path', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph',
            name='node',
            field=models.IntegerField(db_index=True),
        ),
    ]