# Generated by Django 5.0.2 on 2024-02-21 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_projectrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectrating',
            name='rating',
            field=models.IntegerField(),
        ),
    ]