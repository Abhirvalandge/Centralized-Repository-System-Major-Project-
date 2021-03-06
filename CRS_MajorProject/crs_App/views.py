import smtplib
from email.message import EmailMessage

from django.core.mail import send_mail, message
from CRS_MajorProject import settings as se
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from crs_App.forms import SignUpForm
from crs_App.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def crs_home_view(request):
    return render(request,"index.html")


def gov_schemes_view(request):
    return render(request,"government_schemes.html")

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['first_name'].upper()
            lastname = form.cleaned_data['last_name'].upper()
            email = form.cleaned_data['email']
            user = form.save()
            user.set_password(user.password)
            user.save()
            subject = "Registration Confirmation Mail"
            user_message = "Hello,\n \"{} {}\" Thanking You for registration".format(firstname,lastname )
            send_mail(subject, user_message, se.EMAIL_HOST_USER, [email])
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html", {'form':form})


def logout_view(request):
    return render(request, "logout.html")

# Schemes List Views-----------------------------------------------
@login_required
def education_list_view(request):
    schemes_list = EducationModel.objects.all()
    main_title = 'Education and Learning'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post=paginator.page(page)
    except PageNotAnInteger:
       post=paginator.page(1)
    except EmptyPage:
        post=paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title,'post':post,'page':page}
    return render(request, 'schemes_list.html', context=my_dict)

@login_required
def health_list_view(request):
    schemes_list = HealthModel.objects.order_by('id')
    main_title = 'Health and Wellness'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, 'schemes_list.html', context=my_dict)

@login_required
def agriculture_list_view(request):
    schemes_list = AgricultureModel.objects.order_by('id')
    main_title = 'Agriculture, Rural and Environment'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, 'schemes_list.html', context=my_dict)

@login_required
def electricity_list_view(request):
    schemes_list = ElectricityModel.objects.order_by('id')
    main_title = 'Electricity, Water and Local Services'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, 'schemes_list.html', context=my_dict)

@login_required
def business_list_view(request):
    schemes_list = BusinessModel.objects.order_by('id')
    main_title = 'Business and Self-employed'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, 'schemes_list.html', context=my_dict)

@login_required
def youth_list_view(request):
    schemes_list = YouthModel.objects.order_by('id')
    main_title = 'Youth Sports and Culture'
    paginator = Paginator(schemes_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'schemes_list': schemes_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, 'schemes_list.html', context=my_dict)

# End Schemes List views----------------------------------------------


# Goverment Jobs views----------------------------------------------
@login_required
def gov_jobs_list_view(request):
    jobs_list = GovernmentJobsModel.objects.order_by('id')
    main_title = 'Government Jobs'
    paginator = Paginator(jobs_list, 2)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    my_dict = {'jobs_list': jobs_list, 'main_title': main_title, 'post': post, 'page': page}
    return render(request, "jobs_list.html", context=my_dict)

# End Government Jobs views----------------------------------------------

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        user_email = request.POST.get("email")
        subject1 = request.POST.get("subject")
        message1 = request.POST.get("message")
        subject = "CRS"
        user_message = "Hello {},\n Thanking you for contac us.!".format(name)
        crs_message = "Sender Name: {}\n Email Id: {}:\n Subject: {}\n Message:{}".format(name,user_email,subject1,message1)
        crs_email = "crsinfo175@gmail.com"
        try:
            send_mail(subject,user_message, se.EMAIL_HOST_USER, [user_email])
            send_mail(subject1,crs_message, se.EMAIL_HOST_USER, [user_email])

            messages.success(request, 'Your message has been sent. Thanking You for contact us!')
            return HttpResponseRedirect('/')
        except smtplib.SMTPAuthenticationError:
            user_mess = EmailMessage(subject, user_message, se.EMAIL_HOST_USER, [user_email])
            crs_mess = EmailMessage(subject1, crs_message, se.EMAIL_HOST_USER, [crs_email])
            user_mess.send(fail_silently=True)
            crs_mess.send(fail_silently=True)
            return HttpResponseRedirect('/')
        except TypeError:
            return HttpResponseRedirect('/')

