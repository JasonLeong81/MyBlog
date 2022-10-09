from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from . import models
from urllib import request
from django.urls import reverse

import MySQLdb

def space():
    # Used for easy
    for i in range(5):
        print('\n')
def index(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="378100Yc", db="blog")
    c = conn.cursor()
    c.execute("""show tables""")
    # r = c.fetchone()
    r = c.fetchall()
    c.close()
    conn.close()
    return HttpResponse(r)
def TN(request,tutorial_number):
    return HttpResponse(f'You are viewing tutorial number : {tutorial_number}')
def t(request):
    # question = get_object_or_404(models.Test, pk=question_id)
    # raise Http404("No tutorials are available.")
    template = loader.get_template('P/index.html')
    context = {'Tutorial_number':[1,2,3,4,5],'he':[1]}
    return HttpResponse(template.render(context, request))
    # return render(request, 'polls/index.html', context) # this is equivalent to return HttpResponse(template.render(context, request))


def detail(request):
    template = loader.get_template('P/detail.html')
    return HttpResponse(template.render({},request))

def run(command):
    # Used in the result function
    conn = MySQLdb.connect(host="localhost", user="root", passwd="378100Yc", db="blog")
    c = conn.cursor()
    c.execute(f"""{command}""")
    conn.commit()
    r = c.fetchall()
    c.close()
    conn.close()
    return r
def result(request):
    template = loader.get_template('P/result.html')
    # run("""insert into test(name,age) values("Jason",20)""")
    r = run("""select * from test""""")
    # space()
    # print(r)
    # r = run("""delete from test""""")
    return HttpResponse(template.render({'r':r},request))

def insert(request):
    if request.method == 'POST':
        conn = MySQLdb.connect(host="localhost", user="root", passwd="378100Yc", db="blog")
        c = conn.cursor()
        name = request.POST['name']
        age = request.POST['age']
        # space()
        # print(name,age)
        # print(request)
        age = int(age)
        c.execute(f"""insert into test(name,age) values("{name}",{age})""")
        conn.commit()
        # r = c.fetchone()
        c.close()
        conn.close()
        return HttpResponseRedirect(reverse('P:detail')) # avoid form resubmission
        # return HttpResponse(r)