# Generated by Django 2.0.2 on 2018-02-25 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]