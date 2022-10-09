from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('NLP/index.html')
    return HttpResponse(template.render({},request))
    # return HttpResponse('NLP')

def Tutorial(request):
    if request.method == 'POST':
        name = request.POST['filename'] # getting the name attribute from button
        try:
            template = loader.get_template(f'NLP/{name}.html')
        except Exception as error:
            print(error)
            return HttpResponse(f'Opps! We are sorry that the {name} tutorial is not available yet, but it will be out soon!')
        else:
            return HttpResponse(template.render({}, request))
    template = loader.get_template('NLP/index.html') # if no button is pressed, we go to index page of NLP
    return HttpResponse(template.render({'r':'Please choose a topic.'}, request))

