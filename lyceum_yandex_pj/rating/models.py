from django.db import models

from catalog.models import Item
from users.models import User


class RatingManager(models.Manager):
    def item_avg_rate(self, item_pk):
        return (
            self.get_queryset()
            .filter(
                item__pk=item_pk,
            )
            .aggregate(
                models.Avg("rate"),
                models.Count("rate"),
            )
        )

    def get_user_rate(self, user_pk, item_pk):
        return (
            self.get_queryset()
            .filter(
                user__pk=user_pk,
                item__pk=item_pk,
            )
            .select_related(
                "item",
                "user",
            )
        ).first()


class Star(models.IntegerChoices):
    HATE = 1, "Ненависть"
    DISLIKE = 2, "Неприязнь"
    NEUTRAL = 3, "Нейтрально"
    ADORATION = 4, "Обожание"
    LIKE = 5, "Любовь"


class ItemRating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=Star.choices)

    objects = RatingManager()

    class Meta:
        unique_together = [("item", "user")]
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    def __str__(self):
        return str(self.id)
