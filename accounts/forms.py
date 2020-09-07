from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid e-mail')

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')  # Username = NIP Number


class AccountEditForm(UserChangeForm):
    co_logo = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Account
        fields = (
            'email',
            'username',  # Username = NIP Number
            'first_name',
            'last_name',
            'language',
            'co_logo',
            'co_name',
            'co_address',
            'co_zip',
            'co_city',
            'co_slogan'
        )


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        # Try to authenticate the form
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")
