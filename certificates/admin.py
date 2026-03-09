from django.contrib import admin
from .models import Certificate, Instrument


class InstrumentInline(admin.TabularInline):
    model = Instrument
    extra = 1


class CertificateAdmin(admin.ModelAdmin):
    inlines = [InstrumentInline]
    search_fields = ['certificate_number']


admin.site.register(Certificate, CertificateAdmin)
