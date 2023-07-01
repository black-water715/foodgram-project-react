from django.apps import AppConfig


class TagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = 'tags'
    name = 'apps.tags'
    verbose_name = 'Теги'