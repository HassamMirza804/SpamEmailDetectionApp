# mlapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from spam_detector.model import predict_message  # Importing from spamdetector

class SomeView(View):
    def post(self, request):
        message = request.POST.get('message')
        result, probability = predict_message(message)

        # Determine alert class based on result
        alert_class = 'danger' if result == 'Spam' else 'success'
        
        return render(request, 'mlapp/home.html', {
            'result': result,
            'probability': probability,
            'alert_class': alert_class,  # Pass alert class to template
        })

def home(request):
    return render(request, 'mlapp/home.html')