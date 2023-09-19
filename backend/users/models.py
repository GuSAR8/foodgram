from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.validators import ValidationError


class User(AbstractUser):
    email = models.EmailField(
        max_length=200,
        unique=True,
        verbose_name='Электронная почта',
    )
    username = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Имя пользователя',
    )
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия'
    )
    password = models.CharField(
        max_length=200,
        verbose_name='Пароль'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscription_user',
        verbose_name='подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscription_author',
        verbose_name='автор',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscription',
            )
        ]

    def clean(self):
        if self.user == self.author:
            raise ValidationError('Нельзя подписаться на себя')

    def __str__(self):
        return f'{self.user} подписан на {self.author}.'
