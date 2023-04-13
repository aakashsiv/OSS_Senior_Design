from django.shortcuts import render
from django.http import JsonResponse
from ml2 import roipred

def my_view(request):
    if request.method == 'POST':
        # process the user's input
        startup_name = request.POST.get('startup-name')  # extract the 'startup-name' field

        # store the startup name in a session variable
        request.session['startup_name'] = startup_name

        # show the progress page
        return render(request, 'progress.html')

    return render(request, 'input_form.html')


def results_view(request):
    # Get the startup name from the session variable
    startup_name = request.session.get('startup_name')
    
    # Perform some operation to get the result
    result = startup_name
    
    # pass ROI to results page
    context = {'result': result}
        
    # return the results page
    return render(request, 'startup_details.html', context)

    
def predict(request):
    import random
    options = ['sell', 'buy']

    # this is my incredibly bad ML model
    result = random.choice(options)
    
    response = {"ticker": "APPL", "action": result}
    return JsonResponse(response)

def homepage(request):
    return render(request, 'homepage.html')