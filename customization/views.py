from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from customization.models import *
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMessage
import random
# Create your views here.

class index(APIView):
    def get(self,request):
        return HttpResponseRedirect('/signup/')

class home(APIView):
    def get(self,request):
        if(request.session.has_key('user')):
            cities=city.objects.all()
            countries = country.objects.all()
            countrylanguages = countrylanguage.objects.values('Language').distinct()
            return render(request,'homepage.html',context={'cities':cities,'countries':countries,'countrylanguages':countrylanguages})
        else:
            return HttpResponseRedirect('/signin/')

class detail(APIView):
    @csrf_exempt
    def post(self,request):
        if(request.session.has_key('user')):
            context_dic = None
            value_obj = None
            name = request.POST.get('name')
            type = request.POST.get('type')
            primary = request.POST.get('primary')
            if type == 'city':
                value_obj = city.objects.get(ID=primary)
                context_dic = {'value_obj': value_obj,'type':type}
            elif type == 'country':
                value_obj = country.objects.get(Code=primary)
                context_dic = {'value_obj': value_obj, 'type': type}
            elif type == 'countrylanguage':
                value_obj = countrylanguage.objects.filter(Language=name)
                context_dic = {'value_obj': value_obj, 'type': type}
            return render(request,'detailpage.html',context=context_dic)
        else:
            return HttpResponseRedirect('/signin/')

class NewSignup(APIView):
    def post(self,request):
        email_id = request.data.get('email')
        firstName = request.data.get('first_name')
        lastName = request.data.get('last_name')
        Gender = request.data.get('gender')
        phoneNumber = request.data.get('phone_number')
        usr = MyUser.objects.create(email=email_id,first_name=firstName,last_name=lastName,gender=Gender,phone_number=phoneNumber)
        usr.save()
        return JsonResponse({'comment':'user saved'})

class VerifyUser(APIView):
    def post(self,request):
        email_id = request.data.get('email')
        otp = random.randint(1000, 9999)
        otp_str = str(otp)
        otp_str = 'otp:' + otp_str
        email = EmailMessage('email verification', otp_str, to=[email_id])
        email.send()
        return JsonResponse({'otp': otp})

class NewSignin(APIView):
    def post(self,request):
        email_id = request.data.get('email')
        request.session['user'] = email_id
        return JsonResponse({'comment':'user signed in'})

class Logout(APIView):
    def post(self,request):
        if(request.session.has_key('user')):
            del request.session['user']
        return HttpResponseRedirect('/signin/')

class signin(APIView):
    def get(self,request):
        users = MyUser.objects.all()
        return render(request,'loginpage.html',context={'users':users})

def countrydetail(request,CountryCode):
    value_obj = country.objects.get(Code=CountryCode)
    return render(request,'countrydetailpage.html',context={'value_obj':value_obj})

class signup(APIView):
    def get(self,request):
        return render(request,'signuppage.html',context=None)