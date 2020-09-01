from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileDeleteForm, UserDeleteForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile_confirm_delete(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/profile_confirm_delete.html', context)

#not sure
def list_all(request):
    context = {
        'users': User.objects.all
    }
    return render(request, 'users/list_all.html', context)

@login_required
def profile(request):
    if request.method == 'DELETE':
        print('delete works')
        return redirect('digitalFarm-home')

    elif request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form. is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)

#@login_required
#def delete_profile(request):
#  if request.method == 'POST':
#    ud_form = UserDeleteForm(request.POST, instance=request.user)
#    pd_form = ProfileDeleteForm(request.POST, request.FILES, instance=request.user.profile)
#    User.objects.get(user=request.user).delete()
    # redirect to some success url
#    if ud_form.is_valid() and pd_form.is_valid():
 #       ud_form.save()
 #       pd_form.save()
 #   messages.success(request, f'Your account has been deleted!')
 #   return redirect('logout')
#  else:
    # access denied
 #   return render(request, 'users/profile_confirm_delete.html')

@login_required
def deleteuser(request):
    if request.method == 'POST':
        delete_form = UserDeleteForm(request.POST, instance=request.user)
        user = request.user
        user.delete()
        messages.info(request, 'Your account has been deleted.')
        return redirect('digitalFarm-home')
    else:
        delete_form = UserDeleteForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'users/profile.html', context)