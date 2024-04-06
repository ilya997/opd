from django import forms

class User(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_repeat = forms.CharField()



