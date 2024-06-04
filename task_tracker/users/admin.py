from django.contrib import admin

from .models import User


class BaseAdmin(admin.ModelAdmin):
	"""Базовая модель админки."""
	empty_value_display = '-пусто-'
	list_per_page = 40


@admin.register(User)
class UserAdmin(BaseAdmin):
	"""Модель админки для Пользователя."""
	fields_to_display_filter_search = (
		'last_name',
		'first_name',
		'username',
		'email',
		'phone'
	)
	list_display = fields_to_display_filter_search
	list_filter = fields_to_display_filter_search
	search_fields = fields_to_display_filter_search
