from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Certificate

@login_required
def search_certificate(request):
    cert = None

    if request.method == "POST":
        certificate_number = request.POST.get("certificate_number")
        instrument_serial = request.POST.get("instrument_serial")
        user = request.user  # only fetch certificates for this user

        try:
            cert = Certificate.objects.get(
                certificate_number=certificate_number,
                instrument=instrument_serial,
                user=user  # ✅ restrict to logged-in user
            )
        except Certificate.DoesNotExist:
            cert = None

    return render(request, "search.html", {"cert": cert})
