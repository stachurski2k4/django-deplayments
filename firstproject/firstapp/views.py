from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from firstapp.forms import NewUserForm,UserProfileInfoForm,UserForm
# Create your views here.
def index(request):
    my_dict={"insert_me": "i am a s/tring"}
    return render(request,'firstapp/index.html',context=my_dict)

def help(request):
    my_dict={"insert_me": "i am a s/tring"}
    return  render(request,'firstapp/help.html',context=my_dict)

def admin(request):
    webpage_list=AccessRecord.objects.order_by('date')
    users=myUser.objects.order_by('user_name')
    date_dict={'access_records': webpage_list,
    'users': users}
    return  render(request,'firstapp/admin.html',context=date_dict)

def mylogin(request):
    form=NewUserForm()
    if(request.method=='POST'):
        form=forms.NewUserForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return index(request)
    _dict={'form':form}
    return render(request,'firstapp/login.html',_dict)

def relative(request):
    _dict={"text":"some text",'number':100}
    return render(request,'firstapp/relative_urls_templates.html',context=_dict)
def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)

            profile.user=user
            if( 'profile_pic' in request.FILES):
                profile.profile_pic=request.FILES['profile_pic']
                print('xd')
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    _dict={'registered':registered,'user_form':user_form,'profile_form':profile_form}
    return render(request,'firstapp/registration.html',context=_dict)


def user_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'firstapp/login.html',{'error':'User is not active'})
        else:
            return render(request,'firstapp/login.html',{'error':'Invalid username or password'})
    else:
        return render(request,'firstapp/login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
