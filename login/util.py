from typing import Optional

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def login(uid: str, password: str) -> Optional[User]:
    user: User = authenticate(username=uid, password=password)
    if user is None:
        return None
    user.save()
    return user
