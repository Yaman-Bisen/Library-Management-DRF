import traceback
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from requests import request, session
from django.http import HttpResponse, JsonResponse
from .models import *
import requests
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
    return render(request, 'LibraryManagement_App/index.html')

@csrf_exempt
def admin_login(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email',None)
            password = request.POST.get('password',None)

            if AdminLogin.objects.filter(email=email, password=password).exists():
                admin_obj = AdminLogin.objects.filter(email=email, password=password).last()
                request.session['admin_email'] = admin_obj.email
                return JsonResponse({'status':'1','msg':'Login successfull...'})
            else:
                return JsonResponse({'status':'0','msg':'Invalid credentials...'})
        except:
            return JsonResponse({'status':'0','msg':'Something went wrong...'})
    else:
        return JsonResponse({'status':'0','msg':'Post method required...'})

@csrf_exempt
def student_login(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email',None)
            password = request.POST.get('password',None)

            if StudentLogin.objects.filter(email=email, password=password).exists():
                student_obj = StudentLogin.objects.filter(email=email, password=password).last()
                request.session['student_email'] = student_obj.email
                return JsonResponse({'status':'1','msg':'Login successfull...'})
            else:
                return JsonResponse({'status':'0','msg':'Invalid credentials...'})
        except:
            return JsonResponse({'status':'0','msg':'Something went wrong...'})
    else:
        return JsonResponse({'status':'0','msg':'Post method required...'})

@csrf_exempt
def student_signup(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email',None)
            password = request.POST.get('password',None)

            if not StudentLogin.objects.filter(email=email).exists():
                try:
                    StudentLogin.objects.create(email=email, password=password)
                    return JsonResponse({'status':'1','msg':'Student registered successfully...'})
                except:
                    return JsonResponse({'status':'0','msg':'Something went wrong...'})
            else:
                return JsonResponse({'status':'0','msg':'Email already exists...'})
        except:
            return JsonResponse({'status':'0','msg':'Something went wrong...'})
    else:
        return JsonResponse({'status':'0','msg':'Post method required...'})

def get_books_list():
    try:
        url = f"{ request.scheme }://{ request.META.get('HTTP_HOST') }/api/bookDetails/"
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        return 'Something weng wrong'
    except:
        return 'Something went wrong'

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_dashboard(request):
    try:
        admin_email = request.session.get('admin_email')
        if admin_email:
            return render(request,'LibraryManagement_App/admin_dashboard.html')
        else:
            return redirect('/')
    except:
        traceback.print_exc()
        return render(request,'LibraryManagement_App/admin_dashboard.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def student_dashboard(request):
    try:
        student_email = request.session.get('student_email')
        if student_email:
            return render(request,'LibraryManagement_App/student_dashboard.html')
        else:
            return redirect('/')
    except:
        pass

def admin_logout(request):
    try:
        if request.session.get('admin_email'):
            del request.session['admin_email']
        return redirect('/')
    except:
        return redirect('/')


def student_logout(request):
    try:
        if request.session.get('student_email'):
            del request.session['student_email']
        return redirect('/')
    except:
        return redirect('/')

