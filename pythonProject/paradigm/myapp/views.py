from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import signup
from django.conf import settings
from django.core.mail import send_mail

# Create your views  here.
def index (request):
    if request.method == 'POST':
       u = str(request.POST['username'])
       e = str(request.POST['staticEmail'])
       p1 = str(request.POST['inputPassword1'])
       p2 = str(request.POST['inputPassword2'])
       f = str(request.POST['fname'])
       l = str(request.POST['lname'])
       if p1==p2:
           us=User()
           us.username=u
           us.email=e
           us.password=p1
           us.first_name=f
           us.last_name=l
           us.save()
           s=signup()
           s.mid=us
           i=request.FILES['img1'];
           s.myprofile=i;
           s.save()

           #subject = 'welcome to portal'
           #message = f'Hi {us.username}, thank you for registering in portal.'
           #email_from = settings.EMAIL_HOST_USER
           #recipient_list = [us.staticEmail, ]
           #send_mail(subject, message, email_from, recipient_list)

           return HttpResponse("Thank you for Signup!")
       else:
           return HttpResponse("Mismatched Password")
    else:
        return render(request,'main.html')

def mydata(request):
    if request.method =='POST':
        e = str(request.POST['staticEmail'])
        p = str(request.POST['inputPassword'])
        print(e, p)
        m = e+" "+p
        print(m)
        return HttpResponse(m)
    else:
        return HttpResponse("we are watching you")


def main(request, id):
    return HttpResponse(id)