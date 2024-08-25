
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("access_report/", views.access_report, name="access_report"),
    path("appointment/", views.appointment, name="appointment"),
    path("bill/", views.bill, name="bill"),
    path("contact/", views.contact, name="contact"),
    path("doctor_appoinment/", views.doctor_appoinment, name="doctor_appoinment"),
    path("doctor_profile/", views.doctor_profile, name="doctor_profile"),
    path("externallogin/", views.externallogin, name="externallogin"),
    path("medicalhistory/", views.medicalhistory, name="medicalhistory"),
    path("patient_profile/", views.patient_profile, name="patient_profile"),
    path("payment/", views.payment, name="payment"),
    path("pharmacist/", views.pharmacist, name="pharmacist"),
    path("prescription/", views.prescription, name="prescription"),
    path("register/", views.register, name="register"),
    path("selectdoctor/", views.selectdoctor, name="selectdoctor"),
    path("view_prescription/", views.view_prescription, name="view_prescription"),
    path("login/", views.login, name="login"),
    path("base/", views.base, name="base"),
    path("logout/", views.logout_view, name="logout"),
    path("pharmacist_profile/", views.pharmacist_profile, name="pharmacist_profile"),
    path("doctor/", views.doctor, name="doctor"),
    path("api/patient_records/", views.patient_record_list, name="patient_record_list"),
    path("api/patient_records/<int:pk>/", views.patient_record_detail, name="patient_record_detail"),
]
