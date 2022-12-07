from datetime import datetime
from django.utils import timezone

from users.models import User


def now():
    return datetime.utcnow()


def get_today_birthday_people(request):
    utctime = now()
    aware_time = timezone.make_aware(utctime, timezone.utc)
    local_time = timezone.localtime(
        aware_time, timezone.get_current_timezone()
    )
    birthdays = (
        User.objects.all()
        .filter(birthday__month=local_time.month, birthday__day=local_time.day)
        .values("email", "first_name")
    )
    return {"birthdays": birthdays, "time": local_time}
