from django import forms


class messageForm(forms.Form):
    message = forms.CharField(max_length=1000)
