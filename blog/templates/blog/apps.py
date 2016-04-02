from django.apps import AppConfig

class BlogConfig(AppConfig):
    name = "blog" # Здесь указываем исходное имя приложения
    verbose_name = "Блог" # А здесь, имя которое необходимо отобразить в админке