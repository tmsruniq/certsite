from django.contrib import admin
from django.urls import path, include
from certificates import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # show logged in user's certificates
    path('', views.my_certificates, name='my_certificates'),

    path('accounts/', include('django.contrib.auth.urls')),
]
