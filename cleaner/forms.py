from django import forms

class RequestForm(forms.Form):
    name = forms.CharField(label='name',max_length=20)
    telephone = forms.IntegerField(label='contact')
    email = forms.EmailField(label='email')
    date = forms.DateField(label='date')
    address = forms.CharField(label='address',max_length=100)
