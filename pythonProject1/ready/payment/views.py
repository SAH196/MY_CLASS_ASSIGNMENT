from django.shortcuts import render,HttpResponse
import stripe
from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def index(request):
    return render(request,'payment / index.html')


def charge(request):  # new
    if request.method == 'POST':
        a = int(request.POST.get('am'))
        charge = stripe.Charge.create(
            amount=a * 100,
            currency='usd',
        source = request.POST['stripeToken'],
        )
        if (charge.status =="succeeded"):
            return HttpResponse("Payment Process Completed")