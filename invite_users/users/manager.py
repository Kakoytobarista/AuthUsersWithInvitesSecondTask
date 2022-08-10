from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User

import uuid

from .utils import process_scoring, create_token
from rating.models import ReferralCode, ReferralRelationship


class CustomUserManager(BaseUserManager):
    """Create custom UserManager with logic for getting points,
    limit on registrations and validations"""
    use_in_migrations = True

    def create_user(self, username: str,
                    email: str, password: str = None,
                    referral_token: uuid = None) -> User:
        """Overridden the create_user UserManager-a method for update
        logic of adding token and process scoring"""
        ref_code = ReferralCode.objects.filter(token=referral_token)
        token = create_token()
        user = self.model(
            username=username, email=self.normalize_email(email), token=token
        )
        user.set_password(password)
        user.save(using=self._db)
        self.create_reftoken(token, user)
        if not referral_token:
            ReferralRelationship(
                inviting=None, invited=user, refer_token=None
            ).save()
            return user

        ReferralRelationship(
            inviting=ref_code[0].user,
            invited=user,
            refer_token=ref_code[0]
        ).save()

        fund = ReferralRelationship.objects.filter(
            refer_token=ref_code[0],
        ).count() + 1
        process_scoring(fund, user)

        return user

    def create_superuser(self, username: str,
                         email: str, password: str = None,
                         token: uuid = None) -> User:
        """Overridden method for creating super user"""
        token = create_token()
        user = self.model(username=username, email=email, token=token)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        ReferralRelationship(
            inviting=None, invited=user, refer_token=None
        ).save()
        self.create_reftoken(token, user)
        return user

    @staticmethod
    def create_reftoken(token: uuid, user: User) -> None:
        """Method for generating referral token"""
        ReferralCode(token=token, user=user).save()
