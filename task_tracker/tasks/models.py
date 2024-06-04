from django.db import models


PROGRESS_CHOICES = (
	('Not started', 'Не начата'),
	('In progress', 'Выполняется'),
	('Completed', 'Завершена')
)

PROGRESS_DEFAULT = PROGRESS_CHOICES[0][0]

PRIORITY_CHOICES = (
	('Urgent', 'Срочно'),
	('Important', 'Важно'),
	('Medium', 'Средний'),
	('Low', 'Низкий')
)

PRIORITY_DEFAULT = PRIORITY_CHOICES[2][0]


class Column(models.Model):
	"""Модель Колонки, в которой будут расположены Задачи."""
	name = models.CharField(
		verbose_name='Колонка',
		max_length=20,
	)

	def __str__(self):
		return self.name


class Tag(models.Model):
	"""Модель Тега, используется для присвоения меток задачам."""
	name = models.CharField(
		verbose_name='Тег',
		max_length=15,
		blank=True,
		null=True,
	)

	def __str__(self):
		return self.name


class ChecklistItem(models.Model):
	"""Модель Чеклиста для присвоения задаче списка подзадач."""
	name = models.CharField(
		verbose_name='Название подзадачи',
		max_length=50,
		blank=True,
		null=True,
	)
	done = models.BooleanField(
		verbose_name='Статус завершения',
		default=False
	)

	def __str__(self):
		return self.name


class Task(models.Model):
	"""Модель Задачи."""
	name = models.CharField(
		verbose_name='Задача',
		max_length=150,
	)
	section = models.ForeignKey(
		'Column',
		verbose_name='Сегмент',
		on_delete=models.CASCADE,
	)
	tag = models.ManyToManyField(
		'Tag',
		verbose_name='Тег',
		blank=True,
	)
	progress = models.CharField(
		verbose_name='Ход выполнения',
		max_length=11,
		choices=PROGRESS_CHOICES,
		default=PROGRESS_DEFAULT
	)
	priority = models.CharField(
		verbose_name='Приоритет',
		max_length=9,
		choices=PRIORITY_CHOICES,
		default=PRIORITY_DEFAULT
	)
	checklist = models.ManyToManyField(
		'ChecklistItem',
		verbose_name='Чеклист',
		blank=True,
	)
	created = models.DateTimeField(
		verbose_name='Создано',
		auto_now_add=True
	)
	start_date = models.DateField(
		verbose_name='Дата начала',
		blank=True,
		null=True,
	)
	end_date = models.DateField(
		verbose_name='Дата завершения',
		blank=True,
		null=True,
	)
	# repeat = ''  # TODO: придумать как реализовать повторение задач
	description = models.TextField(
		verbose_name='Описание',
		blank=True,
		null=True,
	)
	# attachments = ''  # TODO: придумать как реализовать вложения
	comments = models.CharField(
		verbose_name='Комментарии',
		max_length=150,
		blank=True,
		null=True,
	)

	def __str__(self):
		return self.name
