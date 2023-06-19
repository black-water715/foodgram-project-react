# Generated by Django 4.2.2 on 2023-06-18 15:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodgram', '0003_remove_recipe_image_base64'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(help_text='Введите время приготовления (ед. измерения в минутах))', validators=[django.core.validators.MinValueValidator(1, message='Время приготовление должны быть >= 1 минуте.')], verbose_name='Время приготовления в минутах'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1, 'Колличество ингредиента в рецептне должно быть >= 1.')]),
        ),
    ]
