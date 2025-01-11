from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')  # Corrected line

def about(request):
    return render(request, 'about.html')  # Corrected line

def services(request):
    return render(request, 'services.html')  # Corrected line

def project(request):
    return render(request, 'project.html')  # Corrected line




from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Compose email
        email_message = EmailMessage(
            subject=f"New message from {name}",
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email='diawaracheicktidiani@gmail.com',  # Verified email address
            to=['wxsanogodra1969@gmail.com'],
            reply_to=[email],  # User's email for replies
        )

        email_message.send()
        return HttpResponseRedirect(reverse('contact_success'))

    return render(request, 'contact.html')


