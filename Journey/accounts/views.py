from django import forms
from django.shortcuts import render, redirect,get_object_or_404
from accounts.models import User
from django.forms import ModelForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# defining forms here itself in views.py

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
        'password': forms.PasswordInput(),
    }

# defining views using forms and models
# creating function for registration page

def register(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if form.is_valid():
                hib = form.save(commit=False)
                hib.password = make_password(request.POST['password'])
                hib.save()
                return redirect('index')
        else:
            return redirect('register')
            messages.error(request,'Password Mismatch')
    return render(request, 'register.html', {'form': form})

def to_get(request):
    hat = User.objects.all()
    return render(request, 'to_get.html', {'hat': hat})

def to_update(request,pk):
    hik = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=hik)
    if form.is_valid():
        hib = form.save(commit=False)
        hib.password = make_password(request.POST['password'])
        hib.save()
        return redirect('to_get')
    return render(request, 'register.html', {'form': form})

def to_delete(request, pk):
    del_obj = User.objects.get(pk=pk)
    del_obj.delete()
    return redirect('to_get')
# defining functions for login page

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        # import ipdb; ipdb.set_trace()
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'invalid username')
            return redirect('login')
        tat = check_password(password, user.password)
        if tat:
            messages.success(request,'successfully logged In')
            return redirect('success')
        else:
            messages.error(request,'invalid password')
            return redirect('login')
    return render(request,'login.html')

def success(request):
    return render(request,'success.html')

# def logout(request):
#     return
