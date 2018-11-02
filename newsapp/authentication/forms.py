from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'first name'})
    )
    last_name = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'})
    )
    username = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Display Name'})
    )
    email = forms.EmailField(label='', max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )
    password_conf = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'})
    )


class LoginForm(forms.Form):
    email = forms.EmailField(label='', max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(label='', max_length=100, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Password'})
    )

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='', max_length=200, required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )