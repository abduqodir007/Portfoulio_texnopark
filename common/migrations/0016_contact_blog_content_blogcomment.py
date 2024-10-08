# Generated by Django 5.0.7 on 2024-08-07 17:43

import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_alter_blog_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('website', models.CharField(max_length=250, verbose_name='website')),
                ('message', models.TextField(verbose_name='message')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='common.blog', verbose_name='blog')),
            ],
        ),
    ]
