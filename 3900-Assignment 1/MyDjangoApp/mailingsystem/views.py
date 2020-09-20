#from django.shortcuts import render

#Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# our view which is a function named index
@csrf_exempt
def index(request):
    #getting our template
    #template = loader.get_template('index.html')
    if request.method == 'POST':
        #rendering the template in HttpResponse
        #return HttpResponse(template.render())
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        #adding the values in a context variable
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        #getting our showdata template
        template = loader.get_template('showdata.html')

        #returing the template
        return HttpResponse(template.render(context, request))

    else:
        #if post request is not true
        #returing the form template
        template = loader.get_template('index.html')
        return HttpResponse(template.render())