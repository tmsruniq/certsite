from django.contrib import admin
from django.urls import path, include
from certificates import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage (certificate search)
    path('', views.search_certificate, name='search_certificate'),
]
