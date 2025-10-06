from django.contrib import admin
from django import forms
from django.apps import apps
from django.conf import settings
from .models import Category, Location, Post

settings.LANGUAGE_CODE = 'ru-RU'

app = apps.get_app_config('blog')
app.verbose_name = 'Блог'

Category._meta.verbose_name = 'категория'
Category._meta.verbose_name_plural = 'Категории'

Location._meta.verbose_name = 'местоположение'
Location._meta.verbose_name_plural = 'Местоположения'

Post._meta.verbose_name = 'публикация'
Post._meta.verbose_name_plural = 'Публикации'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'slug': 'Идентификатор',
            'is_published': 'Опубликовано',
            'created_at': 'Добавлено',
        }
        help_texts = {
            'is_published': 'Снимите галочку, чтобы скрыть публикацию.',
            'slug': 'Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.',
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'name': 'Название места',
            'is_published': 'Опубликовано',
            'created_at': 'Добавлено',
        }
        help_texts = {
            'is_published': 'Снимите галочку, чтобы скрыть публикацию.',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'pub_date': 'Дата и время публикации',
            'author': 'Автор публикации',
            'category': 'Категория',
            'location': 'Местоположение',
            'is_published': 'Опубликовано',
            'created_at': 'Добавлено',
        }
        help_texts = {
            'is_published': 'Снимите галочку, чтобы скрыть публикацию.',
            'pub_date': 'Если установить дату и время в будущем — можно делать отложенные публикации.',
        }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    form = LocationForm
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'category', 'location', 'is_published', 'pub_date', 'created_at')
    list_filter = ('is_published', 'pub_date', 'created_at', 'category', 'location')
    search_fields = ('title', 'text')
    raw_id_fields = ('author', 'category', 'location')
