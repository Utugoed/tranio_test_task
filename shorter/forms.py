from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(label='url', max_length=150)