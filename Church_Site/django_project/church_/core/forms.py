from django import forms 

class SubscribeForm(forms.form):
    email = forms.EmailField()
