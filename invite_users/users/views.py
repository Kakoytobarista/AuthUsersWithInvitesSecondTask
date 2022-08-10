from django.shortcuts import render
from .forms import SignupForm
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

from django.shortcuts import redirect

from .utils import send_mail_custom
from rating.models import ReferralCode

User = get_user_model()


def signup(request):
    if request.user.is_authenticated:
        return redirect('rating:scores')
    if request.method != 'POST':
        form = SignupForm()
        return render(request, 'users/signup.html', {'form': form})

    form = SignupForm(request.POST)
    if not form.is_valid():
        return render(request, 'users/signup.html', {'form': form})
    user_cnt = User.objects.all().count()
    referral_token = form.cleaned_data['referral_token']

    if not referral_token and user_cnt > 5:
        return render(request, 'users/token_validation/more_5_user_validation.html')

    if referral_token:
        ref_code = ReferralCode.objects.filter(token=referral_token)
        if not ref_code:
            return render(request, 'users/token_validation/invalid_token.html')
    user = form.save(commit=False)
    send_mail_custom(request=request,
                     user=user,
                     form=form)

    user.is_active = False
    user.save()
    return render(request, 'users/confirm_email/confirm_email.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    print(f'Found user: {user}')
    is_token_valid = default_token_generator.check_token(user, token)
    print(f"Token valid: {is_token_valid}")
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/confirm_email/email_confirmed.html')
    return render(request, 'users/confirm_email/invalid_link.html')
