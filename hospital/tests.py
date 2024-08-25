
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import PatientRecord

class PatientRecordTests(TestCase):
    def setUp(self):
        self.patient = get_user_model().objects.create_user(username='patient', password='patientpass', user_type='patient')
        self.doctor = get_user_model().objects.create_user(username='doctor', password='doctorpass', user_type='doctor')
        self.record = PatientRecord.objects.create(patient=self.patient, doctor=self.doctor, diagnosis='Test Diagnosis', prescription='Test Prescription')

    def test_patient_record_creation(self):
        self.assertEqual(self.record.diagnosis, 'Test Diagnosis')
        self.assertEqual(self.record.prescription, 'Test Prescription')
        self.assertEqual(self.record.patient.username, 'patient')
        self.assertEqual(self.record.doctor.username, 'doctor')
