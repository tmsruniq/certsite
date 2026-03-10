from django.contrib import admin
from django.urls import path, include
from certificates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_certificate, name='my_certificates'),
    path('accounts/', include('django.contrib.auth.urls')),
]
