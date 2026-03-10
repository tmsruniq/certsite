from django.shortcuts import render
from .models import Certificate

def search_certificate(request):

    cert = None

    if request.method == "POST":
        certificate_number = request.POST.get("certificate_number")
        instrument_serial = request.POST.get("instrument_serial")

        try:
            cert = Certificate.objects.get(
                certificate_number=certificate_number,
                instrument_serial=instrument_serial
            )
        except Certificate.DoesNotExist:
            cert = None

    return render(request, "search.html", {"cert": cert})
