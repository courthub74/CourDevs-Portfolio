from django.shortcuts import render
from django.core.mail import send_mail

#HomePage
def home(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # Send email
        send_mail(
            "Message from:" + message_name, # Subject
            message, # message
            message_email, # from email
            ['courdevelops@gmail.com'], # To email
            fail_silently=False, # Fail Safe
        )

        return render(request, 'home.html', {'message_name': message_name, 'message_email': message_email, 'message': message})
    
    else:
        # return the page

        return render(request, "home.html", {})

