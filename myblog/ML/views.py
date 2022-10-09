from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('ML/index.html')
    return HttpResponse(template.render({'r':1},request))
    # return HttpResponse('ML')

def remove_underscore(string):
    # Used to show users the name of the topic that is currently not available
    # Assumes that string is stripped of white spaces
    string_without_underscore = ''
    for i in range(0,len(string)):
        if string[i] == '_':
            string_without_underscore += ' '
        else:
            string_without_underscore += string[i]
    return string_without_underscore
def Tutorial(request):
        if request.method == 'POST':
            name = request.POST['filename']  # getting the name attribute from button
            try:
                template = loader.get_template(f'ML/{name}.html')
            except Exception as error:
                print(error)
                return HttpResponse(
                    f'Opps! We are sorry that the {remove_underscore(name)} tutorial is not available yet, but it will be out soon!')
            else:
                return HttpResponse(template.render({}, request))
        template = loader.get_template('ML/index.html')  # if no button is pressed, we go to index page of ML
        return HttpResponse(template.render({'r': 'Please choose a topic.'}, request))