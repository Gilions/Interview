import random
import string

from .models import User


def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


def get_author(user):
    if user.is_anonymous:
        random_username = f"{randomString(10)}_guest"
        random_email = f"{randomString(5)}_guest@example.com"
        guest_user = User.objects.create(
            username=random_username,
            is_active=False,
            email=random_email)
        guest_user.save()
        return guest_user
    else:
        return user
