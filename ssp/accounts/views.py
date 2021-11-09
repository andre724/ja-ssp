from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm , LoginUserForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm()
        
    context = {'form':form}
    if form.errors:
        return render(request, "accounts/register.html", context=context, status= 400 )
    else:
         return render(request, "accounts/register.html", context=context, status= 200)


def login_user(request):
    if request.method== 'POST':
        form = LoginUserForm(request.POST)
        form.is_valid()
        user = authenticate(request,email=form.cleaned_data['email'],password=form.cleaned_data['password'])
        if user is not None:
            login(request, user, backend= user.backend)
            return redirect('/')
        else:
            form = LoginUserForm()
            context= {
            'form':form,
            'user': user }
            return render(request, "accounts/login.html", context= context, status= 400)
    else:
        form = LoginUserForm()
        return render(request, "accounts/login.html", {'form':form})

@login_required
def index(request):
    return HttpResponse(f'You are {request.user}')
