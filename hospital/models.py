

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("pharmacist", "Pharmacist"),
    )
    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default="patient"
    )

class PatientRecord(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'patient'}, related_name='patient_records')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'}, related_name='doctor_records')
    diagnosis = models.TextField()
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.patient.username} - {self.doctor.username}"