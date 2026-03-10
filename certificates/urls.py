from django.contrib import admin
from django.urls import path, include
from certificates import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_certificate, name='search_certificate'),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
