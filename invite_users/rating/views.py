from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


from django.contrib.auth import get_user_model

User = get_user_model()


class RatingView(LoginRequiredMixin, TemplateView):
    """View class for getting context of top inviters"""
    template_name = 'rating/scores.html'
    title = 'Rating'

    def get_context_data(self, **kwargs):
        """overridden get_context method"""
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()[:10]
        return context


class ReferralCodeView(LoginRequiredMixin, TemplateView):
    """View class for getting context of top inviters"""
    template_name = 'rating/referral_code.html'
    title = 'Rating'

    def get_context_data(self, **kwargs):
        """overridden get_context method"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.data['user']
        return context
