from django.urls import path

from .views import RatingView

app_name = 'rating'

urlpatterns = [
    path(
        'scores/',
        RatingView.as_view(),
        name='scores'
    ),
]
