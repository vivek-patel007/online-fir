from django.shortcuts import render, redirect
from django.contrib import messages
from userfir.models import missingPerson, FIR, criminal
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def criminal_view(request):
    crim = criminal.objects.all()
    context = {'criminal': crim}
    return render(request, 'userfir/criminal.html', context)


def criminal_detail(request, criminal_id):
    if criminal_id != "":
        cr = criminal.objects.get(pk=criminal_id)
        context = {'criminal': cr}
    return render(request, 'userfir/criminal_detail.html', context)


def missing_person(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        city = request.POST.get('city_id')
        area = request.POST.get('Area')
        address = request.POST.get('address')
        img = request.FILES.get('image')
        age = request.POST.get('age')
        mobile_no = request.POST.get('mobile_no')
        desc = request.POST.get('description')
        user_rol = request.POST.get('user_role')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        last_seen = request.POST.get('lastseen')
        station = request.POST.get('policestation')
        print("hello")
        if age.isdigit():
            int(age)
        else:
            messages.error(request, 'Invalid Age..')
            return redirect('missing_person')
        if height.isdigit():
            int(height)
        else:
            messages.error(request, 'Invalid Height..')
            return redirect('missing_person')
        if weight.isdigit():
            int(weight)
        else:
            messages.error(request, 'Invalid Weight..')
            return redirect('missing_person')
        if name == "" and city == "" and area == "" and address == "" and img == "" and age == "" and mobile_no == "" and desc == "" and user_rol == "" and height == "" and weight == "" and last_seen == "" and station == "":
            messages.error(request, 'please fill all field ! all fields are required')
            return redirect('missing_person')
        mp = missingPerson(full_name=name, city=city, area=area, address=address, image=img, age=age,
                           mobile_no=mobile_no, description=desc, user_role=user_rol, height=height, weight=weight,
                           last_seen=last_seen, police_station=station)
        print("success")

        mp.save()
        messages.success(request, 'missing person added succesfully...')
        return redirect('missing_person')
    return render(request, 'userfir/missing_person.html')


def person_detail(request, missing_id):
    if missing_id != "":
        mp = missingPerson.objects.get(pk=missing_id)
        context = {'person': mp}
    return render(request, 'userfir/person_detail.html', context)


def edit_profile(request):
    user = get_user_model()
    usr = user.objects.get(username=request.user.username)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        city_id = request.POST.get('city_id')
        address = request.POST.get('address')
        if first_name == "" and last_name == "" and gender == "" and dob == "" and city_id == "" and address == "":
            messages.error(request, 'all field are required, please fill all fields')
            return redirect("edit_profile")
        myuser = user.objects.get(username=request.user.username)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.gender = gender
        myuser.dob = dob
        myuser.city = city_id
        myuser.address = address
        myuser.save()
        messages.success(request, 'your profile has been updated!!!!')
        return redirect("/")

    return render(request, 'userfir/edit_user.html', {'user': usr})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        paswd = request.POST.get('new_password1')
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!

            subject = 'Change Password Details'
            message = "Dear User, \n Your password is changed successfully.\n your Password is .%s \n \n	Thank you " \
                      "for Contacting us Online FIR Team." % (
                          paswd)

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('change_password'))
            # return redirect('change_password')
        else:
            print(form.errors)
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userfir/change_password.html', {'form': form})


def create_fir(request):
    fr = FIR.objects.all()
    context = {'context': fr}
    if request.method == 'POST':
        police_station_name = request.POST.get('police_station_name')
        user_proof = request.FILES.get('user_proof')
        complaint_type = request.POST.get('complaint_type')
        against_whom = request.POST.get('against_whom')
        if police_station_name == "" and user_proof == "" and complaint_type == "" and against_whom == "":
            messages.error(request, 'All fields are required !!!')
            return redirect('create_fir')
        fir = FIR(police_station=police_station_name, user_proof=user_proof, complaint_type=complaint_type,
                  against_whom=against_whom, user_id=request.user.pk)
        fir.save()
        messages.success(request, 'your FIR has been added successfully !!!')
        return redirect('create_fir')
    return render(request, 'userfir/fir.html', context)


def view_fir(request):
    fir = FIR.objects.all()
    return render(request, 'userfir/view_fir.html', {'fir': fir})


def approve_fir(request, fir_id):
    fir = FIR.objects.get(pk=fir_id)
    fir.status = True
    fir.save()
    messages.success(request, 'FIR approved successfully....')
    return HttpResponseRedirect(reverse('view_fir'))


def edit_profile_police(request):
    user = get_user_model()
    usr = user.objects.get(username=request.user.username)

    if request.method == 'POST':
        division = request.POST.get('division')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        website = request.POST.get('website')
        if division == "" and contact_no == "" and website == "" and address == "":
            messages.error(request, 'all field are required, please fill all fields')
            return redirect("edit_profile")
        myuser = user.objects.get(username=request.user.username)
        myuser.division = division
        myuser.website = website
        myuser.address = address
        myuser.contact_no = contact_no
        myuser.save()
        messages.success(request, 'your profile has been updated!!!!')
        return redirect("/")

    return render(request, 'userfir/edit_police.html', {'user': usr})


def forget_password(request):
    user = get_user_model()
    pass_list = ["aqC@491", 'aK1ypsvp1', 'FTMXwhc81', 'Zq87g9po']
    paswd = random.choice(pass_list)
    if request.method == 'POST':
        email_id = request.POST.get('email_id')
        if user.objects.filter(email=email_id).exists():
            u = user.objects.get(email=email_id)
            u.set_password(paswd)
            u.save()

            subject = 'Forgot Password Details'
            message = "Dear User,\nYou have requested to send the password for login.\n So according to " \
                      "your requirement your Password is : %s \n Kindly requesting to you to use " \
                      "this Password for login. \n \nThank you for Contacting us. Crime Online FIR team" % (
                          paswd)

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Mail has been sent successfully !!!")

            return redirect("/")
        else:
            messages.error(request, "Invalid Email Address !!!")
            return redirect("forget_password")
    return render(request, 'userfir/forget_password.html')


def search(request):
    if request.method == 'GET':  # this will be GET now
        name = request.GET.get('search')  # do some research what it does
        status = criminal.objects.filter(
            name__icontains=name)  # filter returns a list so you might consider skip except part
        context = {'data': status}
    else:
        context = {}
    return render(request, "userfir/search.html", context)
