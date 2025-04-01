from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.forms import UserRegisterForm, ProfileForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


# @login_required
# def dashboard(request):
#     return render(request,'account/dashboard.html',{'section': 'dashboard'})



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.forms import UserRegisterForm

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/template/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'account/template/register.html', {'user_form': user_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
            'account/template/register_done.html',
                  {'new_user': new_user})

    else:
        user_form = UserRegisterForm()
    return render(request,
    'account/template/register.html',
                  {'user_form': user_form})


@login_required
def edit_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('edit_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:

        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, 'account/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })



