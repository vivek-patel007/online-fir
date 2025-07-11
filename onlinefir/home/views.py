from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from home.models import contactUs
from django.contrib import messages
from home.models import feedback
from userfir.models import missingPerson


# Create your views here.
def homepage(request):
    mp=missingPerson.objects.all()
    context={'context':mp}
    return render(request, 'home/home.html',context)


def about_usPage(request):
    return render(request, 'home/about.html')


def crime_info(request):
    return render(request, 'home/criminal.html')


def login_handle(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']

            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                # messages.success(request, "login success")
                return HttpResponseRedirect(reverse('homepage'))
    else:
        fm = AuthenticationForm()
    return render(request, 'home/login.html', {'form': fm})


def signup_handle(request):
    if request.method == 'POST':
        tpe = request.POST.get('user_type')
        # print(tpe)
        if tpe == "police":
            return redirect('signup_police')
        else:
            return redirect('signup_user')
    return render(request, 'home/signup.html')


def mail_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        con = contactUs(full_name=name, email=email, subject=subject, msg=message)
        con.save()
        messages.success(request, 'Thank you for contacting us')
        return redirect('/')
    return render(request, 'home/mail.html')


def signup_user(request):
    user = get_user_model()
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        pswd = request.POST.get('pswd')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        city_id = request.POST.get('city_id')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        image = request.FILES.get('image')
        if email_id == "" and pswd == "" and first_name == "" and last_name == "" and gender == "" and dob == "" and city_id == "" and address == "" and contact_no == "" and image == "":
            messages.error(request, "all field are required, please fill all fields.")
            return redirect("signup_user")
        if user.objects.filter(username=username).exists():
            messages.error(request, "This UserName Is Already Available.")
            return redirect("signup_user")
        if len(username) > 15:
            messages.error(request, "User Name Must Be 15 Characters.")
            return redirect("signup_user")
        if not username.isalnum():
            messages.error(request, "Username Should Only Contain Letters And Numbers.")
            return redirect("signup_user")
        myuser = user.objects.create_user(username, email_id, pswd)
        myuser.gender = gender
        myuser.dob = dob
        myuser.city = city_id
        myuser.address = address
        myuser.contact_no = contact_no
        myuser.image = image
        myuser.is_user = True
        myuser.save()
        messages.success(request,'your account created successfully..you can now login to your acocount..')
        return redirect("loginpage")

    return render(request, 'home/signup_user.html')


def signup_police(request):
    user = get_user_model()
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        pswd = request.POST.get('pswd')
        username = request.POST.get('username')
        division = request.POST.get('division')

        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        website = request.POST.get('website')

        if email_id == "" and pswd == "" and division == "" and website == "" and address == "" and contact_no == "" and username == "":
            messages.error(request, "all field are required, please fill all fields.")
            return redirect("signup_police")
        if user.objects.filter(username=username).exists():
            messages.error(request, "This UserName Is Already Available.")
            return redirect("signup_police")
        if len(username) > 15:
            messages.error(request, "User Name Must Be 15 Characters.")
            return redirect("signup_police")
        if not username.isalnum():
            messages.error(request, "Username Should Only Contain Letters And Numbers.")
            return redirect("signup_police")
        myuser = user.objects.create_user(username, email_id, pswd)
        myuser.address = address
        myuser.contact_no = contact_no
        myuser.division = division
        myuser.website = website
        myuser.is_police = True
        myuser.gender = "OTHER"
        myuser.city = "CITY"

        myuser.save()
        messages.success(request, 'your account created successfully..you can now login to your acocount..')
        return redirect("loginpage")
    return render(request, 'home/signup_police.html')


def logouthandle(request):
    logout(request)
    request.session.flush()
    #  messages.success(request, "logout success")
    return redirect("loginpage")


def forgot_password(request):
    subject = 'welcome to GFG world'
    message = f'Hi , thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = 'vp67176@gmail.com'
    send_mail(subject, message, email_from, recipient_list)


def feedback_view(request):
    if request.method == 'POST':
        email = request.POST.get('email_id')
        msg = request.POST.get('message')
        if msg == "":
            messages.error(request, 'Please fill the message !!!')
            return redirect('feedback_view')
        fb = feedback(email_id=email, message=msg)
        fb.save()
        messages.success(request, 'Thank you for your valuable feedback!we will get back to you soon!')
        return redirect('feedback_view')
    return render(request, 'home/feedback.html')
