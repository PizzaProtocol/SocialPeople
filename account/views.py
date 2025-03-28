from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.forms import UserRegisterForm


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

            return render(request, 'account/template/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegisterForm()
    return render(request, 'account/template/register.html', {'user_form': user_form})