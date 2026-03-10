from django.contrib import admin
from django.urls import path, include
from certificates import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_certificate, name='search_certificate'),
    path('accounts/', include('django.contrib.auth.urls')),
]
