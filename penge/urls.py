from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('', include('accounts.urls')),
    path('', include('website.urls')),
    path('', include('blog.urls')),
    path('', include('feedback.urls')),
    path('dashboard/', include('dashboard.urls')),

    # 3th Party
    path('tinymce/', include('tinymce.urls')),
    path('inbox/notifications/', include('notifications.urls')),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
