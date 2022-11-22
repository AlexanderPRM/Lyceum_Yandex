from django.db import models


class FeedBack(models.Model):
    text = models.TextField(verbose_name='Содержимое')
    mail = models.EmailField(verbose_name='Почта', max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
