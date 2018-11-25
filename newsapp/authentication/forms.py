from django import forms
from parsley.decorators import parsleyfy


@parsleyfy
class RegisterForm(forms.Form):
    first_name = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'first name'})
    )
    last_name = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    username = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Display Name'})
    )
    email = forms.EmailField(label='', min_length=2, max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password_conf = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        parsley_extras = {
            'password_conf': {
                'equalto': "password",
                'error-message': "Your passwords do not match.",
            },
        }


@parsleyfy
class LoginForm(forms.Form):
    email = forms.EmailField(label='', min_length=2, max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(label='', min_length=2, max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )

@parsleyfy
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='', min_length=2, max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )