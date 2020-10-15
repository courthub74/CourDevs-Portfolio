from django.shortcuts import render

#HomePage
def home(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        return render(request, 'home.html', {'message_name': message_name, 'message_email': message_email, 'message': message})
    
    else:
        # return the page

        return render(request, "home.html", {})

#ContactPage
def contact(request):

        return render(request, 'contact.html', {})
