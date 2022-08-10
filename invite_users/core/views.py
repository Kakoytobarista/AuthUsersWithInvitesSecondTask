from django.http import HttpResponse
from django.shortcuts import redirect, render


def page_not_found(request, exception=None) -> HttpResponse:
    return HttpResponse('Error handler content', status=404)


def csrf_failure(request, reason='') -> HttpResponse:
    return render(request, 'core/403csrf.html')


def server_error(request) -> HttpResponse:
    return render(request, 'core/500.html', status=500)


def redirect_from_index(request) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('rating:scores')
    return redirect('users:login')
