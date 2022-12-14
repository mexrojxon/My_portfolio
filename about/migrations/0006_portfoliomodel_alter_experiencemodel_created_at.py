# Generated by Django 4.1 on 2022-08-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_experiencemodel_alter_educationmodel_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, verbose_name='project_name')),
                ('project_link', models.URLField(verbose_name='project_link')),
                ('image', models.ImageField(upload_to='projects/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
            options={
                'verbose_name': 'portfolio',
                'verbose_name_plural': 'portfolios',
            },
        ),
        migrations.AlterField(
            model_name='experiencemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
    ]
