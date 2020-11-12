from django.shortcuts import render
from staff.models import StaffAccount
from staff.models import StaffAuth
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = StaffAccount.objects.get(email=username)
        userlogin = StaffAuth.objects.get(username=username)

    return render(request, 'account_management/account.html', {'user': user, 'userlogin': userlogin})


def update_account(request):
    username = request.user.username
    if request.method == 'POST':
        if request.POST.get('email'):
            StaffAccount.objects.filter(email=username).update(
                email=request.POST.get('email')
            )
        if request.POST.get('fname'):
            StaffAccount.objects.filter(email=username).update(
                fname=request.POST.get('fname')
            )
        if request.POST.get('lname'):
            StaffAccount.objects.filter(email=username).update(
                lname=request.POST.get('lname')
            )
        if request.POST.get('title'):
            StaffAccount.objects.filter(email=username).update(
                job_title=request.POST.get('title')
            )
        user = StaffAccount.objects.get(email=username)
        userlogin = StaffAuth.objects.get(username=username)
        return render(request, 'account_management/account.html', {'user': user, 'userlogin': userlogin})
