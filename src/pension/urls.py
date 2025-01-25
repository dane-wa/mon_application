from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('retraite.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
# Ajouter la configuration pour servir les fichiers statics pendant le developpement
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )