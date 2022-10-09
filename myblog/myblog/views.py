from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader



def index(request):
    template = loader.get_template('P/Home.html')
    return HttpResponse(template.render({},request))

