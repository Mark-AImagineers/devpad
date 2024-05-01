from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
@login_required
def main_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {
            'username': username,
        }
        return render(request, 'projectmgmt/maindash.html', context)
    else:
        messages.error(request, 'You need to login first')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/accounts/login')