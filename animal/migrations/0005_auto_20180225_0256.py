# Generated by Django 2.0.2 on 2018-02-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0004_animal_adoption_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='types',
            field=models.ManyToManyField(to='animal.Type'),
        ),
    ]
