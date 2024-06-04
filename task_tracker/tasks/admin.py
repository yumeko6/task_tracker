from django.contrib import admin

from tasks.models import ChecklistItem, Tag, Task, Column


class BaseAdmin(admin.ModelAdmin):
	"""Базовая модель админки."""
	empty_value_display = '-пусто-'
	list_per_page = 40


@admin.register(Column)
class ColumnAdmin(BaseAdmin):
	"""Панель админки для Колонки."""
	fields_to_display_filter_search = (
		'name',
	)
	list_display = fields_to_display_filter_search
	search_fields = fields_to_display_filter_search


@admin.register(ChecklistItem)
class ChecklistItemAdmin(BaseAdmin):
	"""Панель админки для Чеклиста."""
	fields_to_display_search = (
		'name',
		'done',
	)
	list_display = fields_to_display_search
	search_fields = fields_to_display_search


@admin.register(Tag)
class ChecklistItemAdmin(BaseAdmin):
	"""Панель админки для Тега."""
	fields_to_display_search = (
		'name',
	)
	list_display = fields_to_display_search
	search_fields = fields_to_display_search


@admin.register(Task)
class TaskAdmin(BaseAdmin):
	"""Панель админки для Задачи."""
	list_display = (
		'name',
		'section',
		'get_tag',
		'progress',
		'priority',
		'created',
		'start_date',
		'end_date',
		'description',
		'comments',
		'get_checklist'
	)
	list_filter = (
		'progress',
		'priority',
		'created',
		'start_date',
		'end_date',
	)
	search_fields = (
		'name',
		'progress',
		'priority',
		'created',
		'start_date',
		'end_date',
		'description',
		'comments',
	)

	@staticmethod
	def get_tag(obj):
		return "\n".join([t.name for t in obj.tag.all()])

	@staticmethod
	def get_checklist(obj):
		return "\n".join([c.name for c in obj.checklist.all()])
