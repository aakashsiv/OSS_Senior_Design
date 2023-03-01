from django.shortcuts import render
from django.http import JsonResponse

def my_view(request):
    if request.method == 'POST':
        # process the user's input
        startup_name = request.POST.get('startup_name')
        # perform some operation using the startup_name input
        result = startup_name
        # return a response
        return render(request, 'startup_details.html', {'result': result})
    else:
        # display the input form
        return render(request, 'input_form.html')
    
def predict(request):
    import random
    options = ['sell', 'buy']

    # this is my incredibly bad ML model
    result = random.choice(options)
    
    response = {"ticker": "APPL", "action": result}
    return JsonResponse(response)