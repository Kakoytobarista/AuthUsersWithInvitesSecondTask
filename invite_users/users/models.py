import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.db import models

from enums.user_enum import UserEnum
from .manager import CustomUserManager


class User(AbstractUser):
    """
    Reimplemented the User model to add token,
    score and add custom manager fields to it.
    """

    username = models.CharField(
        error_messages=UserEnum.USERNAME_ERROR_MESSAGE.value,
        help_text=UserEnum.USERNAME_HELP_TEXT.value,
        max_length=UserEnum.USERNAME_MAXLENGTH.value,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
        verbose_name=UserEnum.USERNAME_VERBOSE_NAME.value,
    )
    password = models.CharField(
        max_length=UserEnum.PASSWORD_MAX_LENGTH.value,
        verbose_name=UserEnum.PASSWORD_VERBOSE_NAME.value,
        validators=[validate_password],
    )
    email = models.EmailField(
        max_length=UserEnum.EMAIL_MAX_LENGTH.value,
        verbose_name=UserEnum.EMAIL_VERBOSE_NAME.value,
        unique=True,
    )
    token = models.UUIDField(
        verbose_name=UserEnum.INVITE_CODE.value,
        unique=True)
    score = models.PositiveIntegerField(verbose_name=UserEnum.SCORE.value,
                                        unique=False,
                                        default=0)
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = UserEnum.USER_VERBOSE_NAME.value
        verbose_name_plural = UserEnum.USER_VERBOSE_NAME_PLURAL.value
        ordering = ['-score']
