from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    certificate_file = models.FileField(upload_to='media/certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate_number


class Instrument(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    instrument_serial = models.CharField(max_length=100)
    instrument_name = models.CharField(max_length=200)

    def __str__(self):
        return self.instrument_serial
