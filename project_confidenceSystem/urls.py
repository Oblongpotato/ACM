from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('app_Chats.urls')),
    path('', include('app_ModelTrainer.urls')),
]

# Add static mapping for 'image_sample' directory during development
if settings.DEBUG:
    urlpatterns += static('/image_sample/', document_root=os.path.join(settings.BASE_DIR, 'image_sample'))

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)