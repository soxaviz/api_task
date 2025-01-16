from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(
        max_length=250,
        verbose_name='название задачи'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='')

    due_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    user = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE,
        verbose_name='автор задачи',
        blank=False,

    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name='Задача'
        verbose_name_plural='Задачи'


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Задача'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Задача-{self.task}: {self.author.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
