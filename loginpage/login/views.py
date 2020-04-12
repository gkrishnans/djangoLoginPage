from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from login.models import log

# Create your views here.
class loginpage(TemplateView):
    template_name = 'loginpage.html'

def data(request):
    user = str(request.POST['UserName'])
    password = str(request.POST['Password'])
    try:
        t = log.objects.get(studentcode = user)
        if(str(t.dob) == password):
            return render(request,'loggedinpage.html',{'code': t.studentcode , 'name': t.studentname , 'admin': t.adminno , 'class' : t.classname ,
            'section': t.section , 'result' : t.result})
        else:
            return render(request,"failed.html ")
    except:
        return render(request,"failed.html")
