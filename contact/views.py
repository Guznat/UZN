from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.views import View
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import requests
from gallery.models import Photo
from random import randint



class EmailView(View):
    def get(self, request):
        form = ContactForm()
        ctx = {
            'form': form
        }
        return render(request, 'contact/contact_box.html', ctx)

    def post(self, request):
        form = ContactForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] + "\n\n\n|Message from: " + form.cleaned_data[
                'from_email'] + "|\n" + "|Tel: " + str(form.cleaned_data['tel_number']) + "|"

            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            if result['success']:
                try:
                    send_mail(subject, message, 'AAAA', ['mojdjango@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Znaleziono błąd. Proszę spróbować ponownie.')
                messages.success(request, 'Wiadomość zostala wysłana!')

            else:
                messages.error(request, 'Zła reCAPTCHA. Proszę spróbować ponownie.')

        return render(request, 'contact/contact_box.html', ctx)


def homepage(request):
    count = Photo.objects.count()
    random_object = Photo.objects.all()[randint(0, count - 1)]
    random_object2 = Photo.objects.all()[randint(0, count - 1)]
    random_object3 = Photo.objects.all()[randint(0, count - 1)]
    ctx = {'random_object': random_object,
           'random_object2': random_object2,
           'random_object3': random_object3,
           }
    return render(request, 'homepage.html', ctx)


def faq(request):
    return render(request, 'FAQ.html')
