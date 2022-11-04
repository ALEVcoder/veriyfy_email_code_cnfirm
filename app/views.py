from django.http import HttpResponse
from django.shortcuts import render, redirect

from veryfiy.settings import EMAIL_HOST_USER
from .models import Code
from django.core.mail import send_mail

from .forms import RegistrationsForm, EmailVerifacationForm, LoginForm
from django.contrib.auth import authenticate, login, get_user_model, logout

User = get_user_model()
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationsForm(request.POST)
        # for user in User.objects.filter(is_verified=False):
        #     user.delete()
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            email = request.POST.get('email')

            user = authenticate(username=username, password=password)
            if user:
                user_code = Code.objects.create(user=user)
                user_code.genarate_code
                if user_code.number:
                    send_mail('Verification code', str(user_code.number), EMAIL_HOST_USER, [email, ])
                    return render(request, 'verify.html', {'id': user.id})
            return redirect('register')
    return render(request, 'register.html')

def resend_code(request, id):
    user = User.objects.get(id=id)
    user_code = Code.objects.get(user=user)
    user_code.genarate_code
    send_mail('Verification code', str(user_code.number), EMAIL_HOST_USER, [user.email])
    return render(request, 'verify.html', {'id': id})

def verify(request, id):
    if request.method == 'POST':
        form = EmailVerifacationForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=int(id))
            number = request.POST.get('code')
            own_code = Code.objects.get(user_id=user.id)
            print(number, own_code, number == own_code)
            if str(number) == str(own_code):
                login(request, user)
                user.is_verified = True
                user.save()
                return redirect('index')
            return HttpResponse("Error")


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
          
            if user:
                login(request, user)
                return redirect('index')
            return redirect('login')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('login')