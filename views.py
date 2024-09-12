from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment, MedicationReminder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    if hasattr(request.user, 'patient'):
        appointments = Appointment.objects.filter(patient=request.user.patient)
        reminders = MedicationReminder.objects.filter(patient=request.user.patient)
        return render(request, 'patient/error.html', {'appointments': appointments, 'reminders': reminders})
    else:
        return render(request,'patient/dashboard.html')

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        description = request.POST.get('description')
        doctor = User.objects.get(id=doctor_id).doctor
        patient = request.user.patient
        Appointment.objects.create(patient=patient, doctor=doctor, date=date, description=description)
        return redirect('dashboard')
    doctors = User.objects.filter(is_staff=True)
    return render(request, 'patient/schedule_appointment.html', {'doctors': doctors})

@login_required
def add_reminder(request):
    if request.method == 'POST':
        medication = request.POST.get('medication')
        reminder_time = request.POST.get('reminder_time')
        patient = request.user.patient
        MedicationReminder.objects.create(patient=patient, medication=medication, reminder_time=reminder_time)
        return redirect('dashboard')
    return render(request, 'patient/add_reminder.html')
