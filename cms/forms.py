from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'body', 'author', 'published_date']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=200)