from django.shortcuts import render
from .models import Certificate

def search_certificate(request):
    cert = None

    if request.method == "POST":
        cert_no = request.POST.get("certificate_number")
        serial = request.POST.get("instrument_serial")

        cert = Certificate.objects.filter(
            certificate_number=cert_no,
            instrument_serial=serial
        ).first()

    return render(request, "search.html", {"cert": cert})
