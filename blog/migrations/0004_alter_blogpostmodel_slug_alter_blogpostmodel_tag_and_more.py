# Generated by Django 4.1 on 2023-06-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='slug',
            field=models.SlugField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='blogpostmodel',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='post', to='blog.tagmodel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created_at'),
        ),
    ]
