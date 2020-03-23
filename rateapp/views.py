from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import auth,User
# Create your views here.
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Module,Professor,RateInfo,Results
from .serializers import ModuleSerializers,Result2Serializers,RateSerializers
#from django.views.decorators.csrf import csrf_exempt
# Create your views here.
user1 =''
#@csrf_exempt
@api_view(['GET','POST'])
def register(request):
    if request.method == 'POST':
        usr = request.POST.get('name')
        pwd = request.POST.get('pwd')

        user_info = User.objects.create_user(username=usr, password=pwd)
        return HttpResponse('resgiter successful!')
#@csrf_exempt
@api_view(['GET','POST'])
def my_view(request):
    if request.method == 'POST':
        usr1 = request.POST.get('name')
        pwd1 = request.POST.get('pwd')

    user_obj=authenticate(username=request.POST.get('name'), password=request.POST.get('pwd'))
    if user_obj:
        login(request,user_obj)
        request.session['user']=usr1
        print(request.session.get('user'))
        request.session.save()
        return HttpResponse('login successful!')
    else:
        return HttpResponse('Error!Please input right infomation')
#@csrf_exempt
@api_view(['GET','POST'])
def logout_view(request):
  logout(request)
  return  HttpResponse('logout successful!')
#@csrf_exempt
@api_view(['GET','POST'])
def list(request):
      modules = Module.objects.order_by('-id')
      if request.method == 'GET':
          serializer = ModuleSerializers(modules,many=True)
          return Response(serializer.data)

#@csrf_exempt
@api_view(['GET', 'POST'])
def view(request):
    professor= Professor.objects.all()
    for p in professor:
        name=p.Name
        rate = RateInfo.objects.filter(Professor=name).all()

        value = 0
        i=0
        for r in rate:
            value=value+r.Rate
            i+=1
        if i:
            value=int(value/i)

        Results.objects.get_or_create(Name=name, Rate=value)

    results = Results.objects.exclude(Rate=0)
    if request.method == 'GET':
        serializer = Result2Serializers(results,many=True)
        return Response(serializer.data)


#@csrf_exempt
@api_view(['GET', 'POST'])
def avr(request):
    if request.method=='POST':

        name = request.POST.get('name')
        professor = request.POST.get('professor')
        module = Module.objects.filter(Code=name)
        if module.count()==0:
            return HttpResponse('Error!Please input right course')
        else:
            pro = Professor.objects.filter(Code=professor)
            if pro.count()==0:
                return HttpResponse('Error!Please input right professor')
            else:
                module = Module.objects.get(Code=name,Semester=1)
                pro = Professor.objects.get(Code=professor)
                name = module.Name
                professor=pro.Name

                rate1 = RateInfo.objects.exclude(Semester=0)
                rate = rate1.filter(Name=name,Professor=professor).all()
                ra=0
                i=0
                for r in rate:
                    ra=ra+r.Rate
                    i=i+1
                if i:
                    ra=int(ra/i)
                RateInfo.objects.get_or_create(Name=name,Professor=professor,Semester=0,Rate=ra)
                rate = RateInfo.objects.filter(Semester=0)
                rate1 = rate.filter(Name=name,Professor=professor)
                serializer = RateSerializers(rate1, many=True)
                return Response(serializer.data)


#@csrf_exempt
@api_view(['POST'])
@login_required
def add_rate(request):
        if request.method == 'POST':
            name = request.POST.get('name1')
            professor = request.POST.get('professor')
            ss = request.POST.get('ss')
            year = request.POST.get('y')
            rr = request.POST.get('r')
            module = Module.objects.filter(Code=name,Semester=ss,Year=year)

            username = request.session.get('user')

            if module.count()>0:
                module = Module.objects.get(Code=name, Semester=ss, Year=year)
                pro = Professor.objects.filter(Code=professor)
                if pro.count()>0:
                    pro = Professor.objects.get(Code=professor)
                    name = module.Name
                    professor = pro.Name
                    rate1 = RateInfo.objects.filter(Name=name, Semester=ss, Professor=professor, Year=year, User=username)
                    if rate1.count()>0:
                        return HttpResponse('Error!The rateing has exits another one!')

                    else:
                        rate = RateInfo()
                        rate.Name = name
                        rate.Professor = professor
                        rate.Semester = ss
                        rate.User = username
                        rate.Year = year
                        rate.Rate = rr
                        rate.save()

                        return HttpResponse(
                            'Add succcessful!')

                else:
                    return HttpResponse('Error!Please input right professor')

            else:
                return HttpResponse('Error!Please input right course')
#@csrf_exempt
@login_required()
def test(request):
    usr=request.session.get('user')

    return HttpResponse(usr)