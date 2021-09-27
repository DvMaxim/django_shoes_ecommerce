from django import forms


class Product(forms.Form):
    count = forms.IntegerField(label='Количество')


class Contact(forms.Form):
    letter = forms.CharField(label="Ваше сообщение", widget=forms.Textarea)
    email = forms.EmailField(label="Ваша почта")