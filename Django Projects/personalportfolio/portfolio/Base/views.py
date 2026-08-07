from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from Base import models

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content') 
        number = request.POST.get('number')
        print(name, email, content, number)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request, 'Name must be between 2 and 30 characters')
            return render(request, 'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request, 'Email must be between 2 and 30 characters')
            return render(request, 'home.html')
        
        if len(number)>2 and len(number)<13:
            pass
        else:
            messages.error(request, 'Number must be between 3 and 12 characters')
            return render(request, 'home.html')
        ins=models.Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Your message has been sent successfully!')
        print(' data saved')
        print('the request is no pass')
    
    return render(request, 'home.html')