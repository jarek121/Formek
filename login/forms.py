from django import forms

class LoginForm(Forms.Form):
    username = forms.CharField()
    password = forms.CharField(Widget=forms.PasswordInput)
