from django.contrib import admin
from django.urls import path
from certificates import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage search
    path('', views.search_certificate, name='search_certificate'),
]

# serve media files (certificate PDFs)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
