from django.db import models
from django.conf import settings

from enums.rating_enum import RatingEnum


class ReferralRelationship(models.Model):
    """Model for crating connect from inviter to invited"""
    inviting = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name=RatingEnum.INVITING.value,
        verbose_name=RatingEnum.INVITING.value,
        on_delete=models.CASCADE,
        null=True,
    )
    invited = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name=RatingEnum.INVITED.value,
        verbose_name=RatingEnum.INVITED.value,
        on_delete=models.CASCADE,
    )
    refer_token = models.ForeignKey(
        RatingEnum.REFERRAL_CODE.value,
        verbose_name=RatingEnum.REFERRAL_CODE.value,
        on_delete=models.CASCADE,
        null=True,
        db_index=True,
    )

    def __str__(self) -> str:
        return f"{self.inviting}_{self.invited}"


class ReferralCode(models.Model):
    """Model for connect token to user"""
    token = models.UUIDField(unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=RatingEnum.USER_VERBOSE_NAME.value,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'token'], name='unique user token')]

    def __str__(self) -> str:
        return f"{self.user}_{self.token}"
