from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
from django.contrib import messages

load_dotenv()

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email alreay in use,Try again!')
            return redirect('signup')
        elif  User.objects.filter(username=username).exists():
            messages.error(request,'Username already in use,Try again!')
            return redirect('signup')
        else:
            otp = send_otp(email)

            user=User.objects.create_user(
                email=email,
                username=username,
                password=password
            )
            Profile.objects.create(
                user=user,
                otp=otp
            )
            messages.success(request,'OTP send successfully to your mail.')
            return redirect('verify')
    return render(request,'signup.html')

def send_otp(email):
    otp=random.randint(111111,999999)
    send_mail(
        subject='otp for verification',
        message=f'the otp is {otp}',
        from_email=os.getenv('EMAIL_HOST_USER'),
        recipient_list=[email],
        fail_silently=True
    )
    return otp

def verify(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')

        if Profile.objects.filter(otp=otp).exists():
            profile = Profile.objects.get(otp=otp)

            if profile.verified == True:  # Correct → no quotes
                request.session['email'] = profile.user.email
                return redirect('password_change')
            
            else:
                profile.verified = True
                profile.save()
                request.session['username'] = profile.user.username
                return redirect('home')

    return render(request, 'verify.html')


def password_change(request):
    if request.method == 'POST':
        new_password = request.POST.get('new-password')
        username=request.session.get('username')
        user=User.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        messages.success(request,'password changed successfully.')
        return redirect('signin')
    return render(request,'password_change.html')

def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.get(username=username)
        existing_user=Profile.objects.get(user=user)

        if user.check_password(password) and  existing_user.verified == True:
            request.session['username']=user.username
            return redirect('home')
        elif existing_user.verified == False:
            email=user.email
            otp=send_otp(email)
            existing_user.otp=otp
            existing_user.save()
            messages.error(request,'OTP send to your email,Please check.')
            return redirect('verify')
        else:
            messages.error(request,'No account found!')
    return render(request,'signin.html')

def forgot(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('email_or_username')
        query = (User.objects.filter(username=email_or_username))| (User.objects.filter(email=email_or_username))
        if not query.exists():
            messages.error(request,'no account found !')
        else:
            try:
                user = User.objects.get(username = email_or_username)
            except:
                user = User.objects.get(email = email_or_username)
            profile=Profile.objects.get(user=user)

            otp = send_otp(user.email)
            profile.otp = otp
            profile.save()
            messages.success(request,'OTP send to mail successfully.')
            return redirect('verify')

    return render(request,'forgot.html')

def home(request):
    return render(request,'home.html',{'username':request.session.get('username')})

def logout(request):
    request.session.flush()
    return redirect('signup')