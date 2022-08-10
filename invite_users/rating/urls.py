from django.urls import path

from .views import RatingView, ReferralCodeView

app_name = 'rating'

urlpatterns = [
    path(
        'scores/',
        RatingView.as_view(),
        name='scores'
    ),
    path(
        'referral_code/',
        ReferralCodeView.as_view(),
        name='referral_code'
    )
]
