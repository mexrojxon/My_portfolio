# Generated by Django 4.1 on 2024-01-08 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_alter_educationmodel_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='phone'),
        ),
    ]