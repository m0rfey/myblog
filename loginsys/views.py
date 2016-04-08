from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from loginsys.forms import registrationsForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return_path = request.META.get('HTTP_REFERER', '/')
            args['login-true'] = "Поздравлаем вы вошли"
            return redirect('/')
        else:
            args['login_error'] = "Внимание! Не коректно введены данные"
            return render_to_response('loginsys/login.html', args)
    else:

        return render(request, 'loginsys/login.html', args)

def logout(request):
    auth.logout(request)
    return_path = request.META.get('HTTP_REFERER', '/')

    return redirect(return_path)

def register(request):
    args={}
    args.update(csrf(request))
    args['form'] = registrationsForm()
    if request.POST:
        newuser_form = registrationsForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form']=newuser_form
    return render(request, 'loginsys/register.html', args)

