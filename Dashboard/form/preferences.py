from django import forms

class FapMaster(forms.Form):
    publicize_log = forms.BooleanField(required=False)  