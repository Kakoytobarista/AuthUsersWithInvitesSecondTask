import enum


class UserEnum(enum.Enum):

    USER_VERBOSE_NAME = 'User'
    USER_VERBOSE_NAME_PLURAL = 'Users'

    BIO_VERBOSE_NAME = 'Bio'

    EMAIL_VERBOSE_NAME = 'Email'
    EMAIL_MAX_LENGTH = 254

    USERNAME_VERBOSE_NAME = 'Username'
    USERNAME_ERROR_MESSAGE = {
        'unique': 'User with that username is present.'
    }
    USERNAME_HELP_TEXT = 'Not more 150 symbols, letters, numbers и @/./+/-/_ only.'
    USERNAME_MAXLENGTH = 150

    PASSWORD_VERBOSE_NAME = 'Password'
    PASSWORD_MAX_LENGTH = 100

    FIRST_NAME_VERBOSE_NAME = 'Name'
    FIRST_NAME_MAX_LENGTH = 150

    LAST_NAME_VERBOSE_NAME = 'Surname'
    LAST_NAME_MAX_LENGTH = 150

    USER_RESET_PASSWORD_ERR_MESSAGE = ('Current password need to be the same with last')
    USER_AUTH_ERR_MESSAGE = ('Check password or try later')

    INVITE_CODE = 'Invite code'

    SCORE = 'Scores'
