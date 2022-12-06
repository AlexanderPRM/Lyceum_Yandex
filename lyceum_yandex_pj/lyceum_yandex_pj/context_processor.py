from datetime import datetime

from users.models import User


def get_today_birthday_people(request):
    birthdays = (
        User.objects.all()
        .filter(birthday__month=datetime.utcnow().month,
                birthday__day=datetime.utcnow().day)
        .values("email", "first_name")
    )
    return {"birthdays": birthdays}
