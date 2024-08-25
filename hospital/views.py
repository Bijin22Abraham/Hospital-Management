from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PatientRecord
from .serializers import PatientRecordSerializer


# # Hardcoded credentials
# HARDCODED_CREDENTIALS = {
#     "doctor": {"username": "doctor", "password": "doctorpass"},
#     "pharmacist": {"username": "pharmacist", "password": "pharmacistpass"},
#     "patient": {
#         "username": "patient",
#         "password": "patientpass",
#     },  
# }


def home(request):
    return render(request, "home.html")


def about(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "about.html")


def access_report(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "access_report.html")


def appointment(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor"]:
        return redirect("login")
    return render(request, "appointment.html")


def bill(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "bill.html")


def contact(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "contact.html")


def doctor_appoinment(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["doctor"]:
        return redirect("login")
    return render(request, "doctor_appoinment.html")


def doctor_profile(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["doctor"]:
        return redirect("login")
    return render(request, "doctor_profile.html")


def externallogin(request):
    return render(request, "externallogin.html")


def medicalhistory(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor"]:
        return redirect("login")
    return render(request, "medicalhistory.html")


def patient_profile(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor"]:
        return redirect("login")
    return render(request, "patient_profile.html")


def payment(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "payment.html")


def pharmacist(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["pharmacist"]:
        return redirect("login")
    return render(request, "pharmacist.html")


def prescription(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "prescription.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def selectdoctor(request):
    return render(request, "selectdoctor.html")


def view_prescription(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient", "doctor", "pharmacist"]:
        return redirect("login")
    return render(request, "view_prescription.html")


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user_type = form.cleaned_data.get("user_type")
            user = authenticate(request, username=username, password=password)
            if user is not None and user.user_type == user_type:
                auth_login(request, user)
                request.session["logged_in"] = True
                request.session["user_type"] = user.user_type
                return redirect("home")
            else:
                messages.error(request, "Invalid username, password, or user type")
        else:
            messages.error(request, "Invalid login credentials")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})


def base(request):
    return render(request, "base.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def selectdoctor(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["patient","doctor"]:
        return redirect("login")
    return render(request, "selectdoctor.html")


def pharmacist_profile(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["pharmacist"]:
        return redirect("login")

    return render(request, "pharmacist_profile.html")


def doctor(request):
    if not request.session.get("logged_in"):
        return redirect("login")
    if request.session.get("user_type") not in ["doctor"]:
        return redirect("login")
    return render(request, "doctor.html")






@api_view(['GET', 'POST'])
def patient_record_list(request):
    if request.method == 'GET':
        records = PatientRecord.objects.all()
        serializer = PatientRecordSerializer(records, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PatientRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def patient_record_detail(request, pk):
    try:
        record = PatientRecord.objects.get(pk=pk)
    except PatientRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientRecordSerializer(record)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
