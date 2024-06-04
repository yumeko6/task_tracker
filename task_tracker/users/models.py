from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def user_images_path(instance, filename) -> str:
    """
    Функция возвращает путь для сохранения аватарки пользователя.
    :param instance: объект модели User
    :param filename: название файла
    :return: путь для сохранения аватарки пользователя
    """
    return f'users/{instance.id}/images/{filename}'


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер. Делает поле username необязательным при создании
    пользователя.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Модель Пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=50,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=50,
    )
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=30,
        blank=True,
        null=True,
        validators=[MinLengthValidator(5)],
    )
    image = models.ImageField(
        verbose_name='Аватарка пользователя',
        upload_to=user_images_path,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=100,
        unique=True,
    )
    phone = PhoneNumberField(
        verbose_name='Телефон',
        max_length=12,
        region='RU',
        blank=True,
        null=True,
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.email
