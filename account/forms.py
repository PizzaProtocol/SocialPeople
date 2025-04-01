from  django import forms
from django.contrib.auth.models import User
from account.models import Profile

class LoginForm(forms.Form):

    username = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Username'
        }))

    password = forms.CharField(
        label=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Password'}))


class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'placeholder': 'Username'
        }))


    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 'placeholder': 'Email'
        }))

    first_name = forms.CharField(
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )

    password = forms.CharField(label=False,
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Password'
                }))

    password2 = forms.CharField(label=False,
                widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Password'
                }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']


class UserEditForm(forms.ModelForm):

    username = forms.CharField(label=False,
                    widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Username'
                    }))

    email = forms.EmailField(label=False,
                widget=forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Email'
                }))
    first_name = forms.CharField(label=False,
                    widget=forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'First Name'
                    }))

    last_name = forms.CharField(label=False,
                    widget=forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Last Name'
                    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label=False,
                                    widget=forms.DateInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Date'
                                    }))

    photo = forms.ImageField(label=False,
                             widget=forms.FileInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Image'
                             }))

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']



