from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# UserRegisterForm is custom form class that inherits UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #we get the details entered by user wrapped up in POST and form variable is instantiated with it.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been created,login to continue.")
            return redirect('login')


    else:
        form= UserRegisterForm()
    template = loader.get_template('users/register.html')
    context={'form':form}
    return HttpResponse(template.render(context,request))
    # return render(request , 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST , instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()    
            messages.success(request , "Your account details have been updated")
            return redirect('user-profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

        
    template=loader.get_template('users/profile.html')
    
    context={
        'user_update_form' : user_update_form ,
        'profile_update_form' : profile_update_form
    }
    return HttpResponse(template.render(context,request))


