from django.shortcuts import render
from django.core.mail import send_mail

#HomePage
def home(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # Send email
        send_mail(
            "Message from:" + message_name, # Subject
            message_email, # email
            message, # message
            ['courtneyj3470@gmail.com'], # To email
            fail_silently=False, # Fail Safe
        )

        return render(request, 'home.html', {'message_name': message_name, 'message_email': message_email, 'message': message})
    
    else:
        # return the page

        return render(request, "home.html", {})

#ContactPage
def contact(request):

        return render(request, 'contact.html', {})
