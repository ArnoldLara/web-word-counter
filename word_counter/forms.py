from django import forms

class NameForm(forms.Form):
    your_url = forms.CharField(label='URL', max_length=100)