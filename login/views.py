from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from . import models
from . import forms
import os


def index(request):
    pass
    return render(request,"login/index.html")
# login/views.py

def login(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        print(login_form)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # print(password)
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    print(login_form)
    return render(request, 'login/login.html', locals( ))

'''
def login(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        message = "所有字段都必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')  # TODO: redirect() request
                else:
                    message = "密码不正确"
            except:
                message = "用户名不存在"
        return render(request,'login/login.html',{"message":message})
    return render(request,"login/login.html")
'''
def register(request):
    pass
    return render(request,"login/register.html")

def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")