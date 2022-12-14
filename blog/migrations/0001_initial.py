# Generated by Django 4.1 on 2022-08-27 17:21

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, verbose_name='category')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('created_at', models.DateTimeField(verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='description')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='post', to='blog.categorymodel')),
                ('tag', models.ManyToManyField(related_name='post', to='blog.tagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
