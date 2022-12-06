from datetime import date

from users.models import User


def get_today_birthday_people(request):
    birthdays = (
        User.objects.all()
        .filter(birthday=date.today())
        .values("email", "first_name")
    )
    return {"birthdays": birthdays}
