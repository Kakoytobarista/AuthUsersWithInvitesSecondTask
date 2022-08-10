import enum


class RatingEnum(enum.Enum):

    INVITING = 'inviter'
    INVITED = 'invited'
    REFERRAL_CODE = 'ReferralCode'

    USER_VERBOSE_NAME = 'Code owner'
    UNIQUE_CONSTRAINT_NAME = 'unique user token'
    UNIQUE_CONSTRAINT_USER = 'user'
    UNIQUE_CONSTRAINT_TOKEN = 'token'
