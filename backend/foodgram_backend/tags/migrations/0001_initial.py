# Generated by Django 4.2.2 on 2023-06-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название тега', max_length=50, unique=True, verbose_name='Название тега')),
                ('color', models.CharField(help_text='Цветовой HEX-код (например, #49B64E)', max_length=7, unique=True, verbose_name='Цвет в формате HEX-кода')),
                ('slug', models.SlugField(help_text='Введите slug - идентификатор', unique=True, verbose_name='Slug - идентификатор')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='tags_tag_name_3fbe74_idx')],
            },
        ),
    ]
