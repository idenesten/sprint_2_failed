# Generated by Django 3.2 on 2022-04-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_filmwork_file_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='description'),
        ),
    ]
