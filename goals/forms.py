from django import forms


class FormStepOne(forms.Form):
    income = forms.DecimalField(decimal_places=2, max_digits=30)
    expenses = forms.DecimalField(decimal_places=2, max_digits=30)
    salary = forms. DecimalField(decimal_places=2, max_digits=30)
    email = forms.EmailField()


class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)
