from django.shortcuts import render
from django.http import JsonResponse
import json
import pandas as pd
from django.conf import settings
from django.core.mail import send_mail
from email.utils import formataddr
from .models import Organizations
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def autocomplete_org_names(request):
    query = request.GET.get('term', '')
    org_names = Organizations.objects.filter(organization_name__icontains=query).values_list('organization_name', flat=True)
    results = list(set(org_names))  # remove duplicates
    return JsonResponse(results, safe=False)


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        # get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        from_address = formataddr((name, email))

        send_mail(
            subject,
            message,
            from_address,
            [settings.DEFAULT_FROM_EMAIL, "siyaduttsharma@gmail.com"],
            fail_silently=False,
        )

        # render success page
        return render(request, 'contactSuccess.html')

    # render contact form
    return render(request, 'contactUs.html')

def contact_success(request):
    return render(request, 'contactSuccess.html')

def top_picks(request):
    return render(request, 'topPicks.html')


@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        # process the user's input
        startup_name = request.POST.get('startup-name')  # extract the 'startup-name' field
        amount_to_invest = request.POST.get('amount-to-invest')  # extract the 'amount-to-invest' field

        # store the names in a session variable
        request.session['startup_name'] = startup_name
        request.session['amount_to_invest'] = amount_to_invest

        # show the progress page
        return render(request, 'progress.html')

    return render(request, 'input_form.html')


def results_view(request):
    # Get the organization name entered by the user
    startup_name = request.session.get('startup_name')
    amount_to_invest = request.session.get('amount_to_invest')
    
    # Query the database to get the corresponding organization object
    organization = get_object_or_404(Organizations, organization_name=startup_name)
    
    # Get the website from the organization object
    result = float(amount_to_invest) * float(organization.roi)
    
    # Pass the website to the results page
    context = {'startup_name': startup_name, 'result': result, 'amount_to_invest': amount_to_invest}
    
    # Return the results page
    return render(request, 'startup_details.html', context)

def get_more_details(request):
        # Get the organization name entered by the user
    startup_name = request.session.get('startup_name')
    organization = get_object_or_404(Organizations, organization_name=startup_name)
    context = {'organization': organization}
    return render(request, 'details.html', context)

def organization_details(request, id):
    organization = Organizations.objects.get(id=id)
    context = {'organization': organization}
    return render(request, 'details.html', context)
    
def predict(request):
    import random
    options = ['sell', 'buy']

    # this is my incredibly bad ML model
    result = random.choice(options)
    
    response = {"ticker": "APPL", "action": result}
    return JsonResponse(response)

def homepage(request):
    return render(request, 'homepage.html')

def top_picks(request):
    organizations = Organizations.objects.order_by('-roi')[:10]
    context = {'organizations': organizations}
    return render(request, 'topPicks.html', context)
