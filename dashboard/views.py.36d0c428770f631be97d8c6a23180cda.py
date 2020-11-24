from django.shortcuts import render, redirect
from staff.models import StaffAccount
from staff.models import StaffAuth
from django.contrib.auth import logout
from appointments.models import Appointment
# Create your views here.


def index(request):
    username = request.user.username
    user = StaffAccount.objects.get(email=username)
    userID = user.auth_id.id
    userlogin = StaffAuth.objects.get(username=username)
    print(user.auth_id)
    appointments = Appointment.objects.filter(
        staff_id=userID)
    return render(request, 'dashboard/overview.html', {'user': user, 'userlogin': userlogin, 'appointments': appointments})


def logout_btn(request):
    logout(request)
    # messages.info(request, "You have logged out successfully!")
    return redirect('index')
