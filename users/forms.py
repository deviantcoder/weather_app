from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '********', 'type': 'password'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '********', 'type': 'password'})
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. janedoe@email.com', 'type': 'email'}),
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. janedoe123', 'type': 'username'}),
        }

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. janedoe@email.com', 'type': 'email'})
#     )
#     username = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'e.g. janedoe123', 'type': 'username'})
#     )
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '********', 'type': 'password'})
#     )
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': '********', 'type': 'password'})
#     )

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2'
#         ]