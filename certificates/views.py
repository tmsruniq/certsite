from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Certificate

@login_required
def my_certificates(request):
    certs = Certificate.objects.filter(user=request.user)
    return render(request, "certificates.html", {"certs": certs})
