from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, empty_value="as")
    phone = forms.CharField(max_length=20, required=True)
