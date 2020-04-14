from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth



# Create your views here.

def myapp(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['re_pass']

        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username already exist')
                return redirect('/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/')

            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                messages.info(request, 'Registration Successful')
                return redirect('login')

        else:
            messages.info(request, 'Passeword not matching')
            return redirect('/')

    # return redirect('/')
    else:
        return render(request, 'Sign up.html')


def login(request):
    if request.method == 'POST':
        name = request.POST['your_name']
        password = request.POST['your_pass']

        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


"""def reset_pass(request):
    return render(request, 'reset_pass.html')"""
