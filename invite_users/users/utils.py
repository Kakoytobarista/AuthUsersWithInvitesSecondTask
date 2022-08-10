from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http.request import HttpRequest

import uuid

from invite_users import settings
from rating.models import ReferralRelationship


def send_mail_custom(request: HttpRequest, user: User,
                     form):
    """
    Function for send email for confirmation enail address.
    """

    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    token = default_token_generator.make_token(user)
    print(f'token in send_mail_custom {token}')
    message = render_to_string('users/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token,
    })
    to_email = form.cleaned_data.get('email')
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)


def process_scoring(fund: ReferralRelationship,
                    user: ReferralRelationship):
    """
    Function with logic of scoring. - The prize fund for the successful
    use of the invitation code is N points, where N is the current number
    of registered users of the code owner + 1. The prize fund is distributed
    according to the scheme: 1 point to the owner of the code, 1 point to the
    one who attracted the owner, and so on, until one of the conditions
    is reached: an N == 0 b the top of the tree is reached
    In case b and if N > 0 - the user at the top gets the whole value of N
    """

    cur_user = user.invited.first().inviting
    while fund != 0:
        if not cur_user.invited.first().inviting:
            cur_user.score += fund
            cur_user.save()
            return
        cur_user.score += 1
        cur_user.save()
        fund -= 1
        cur_user = cur_user.invited.first().inviting


def create_token() -> uuid:
    """
    Function for generating uuid.
    """

    return uuid.uuid4()
