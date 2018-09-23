from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':  # user has info wants to open account
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])  # check user name already or not
                return render(request, 'account/signup.html', {'error': 'Username already exist'})
            except User.DoesNotExist:  # new user created
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)  # lock details of user
                return redirect('home')  # user successfully login
        else:
            return render(request, 'account/signup.html', {'error': 'Password doesnot match'})

    else:
        # user has already account
     return render(request,'account/signup.html',)

def login(request):
    if request.method == 'POST':
       user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
       # check username and password
       if user is not None:
           auth.login(request,user) #lock details of user if correct
           return redirect('home')
       else:
           return render(request, 'account/login.html',{'error':'Username or Password is Invalid' })
    else:    #not a post requeust
      return render(request,'account/login.html')

def logout(request):
    if request.method == 'POST':# if request is post
        auth.logout(request)
        return redirect('home')
