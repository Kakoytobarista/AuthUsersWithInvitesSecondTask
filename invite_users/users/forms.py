from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput,
                               help_text='Password', )

    class Meta:
        model = User
        fields = (
            'email',
        )

    def save(self, commit: bool = True) -> User:
        user = User.objects.create_user(**self.cleaned_data)
        return user


class SignupForm(UserCreationForm):
    """Model for extending UserCreationForm"""
    email = forms.EmailField(max_length=200, help_text='Required')
    referral_token = forms.UUIDField(
        help_text="Token", required=False, )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            "referral_token",
        )
