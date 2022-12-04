from django.db import models


class FeedBack(models.Model):
    text = models.TextField(verbose_name='содержимое')
    mail = models.EmailField(verbose_name='почта', max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'
