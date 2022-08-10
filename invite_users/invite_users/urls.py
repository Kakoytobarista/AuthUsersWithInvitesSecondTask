from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from invite_users import settings
from core.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('rating/', include('rating.urls', namespace='rating')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = page_not_found
handler403 = 'core.views.csrf_failure'
handler500 = 'core.views.server_error'
