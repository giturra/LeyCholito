# Generated by Django 2.0.2 on 2018-02-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0003_animal_is_adoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='adoption_time',
            field=models.DateField(null=True),
        ),
    ]