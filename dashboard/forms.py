from django import forms

from .models import Client, Invoice, InvoiceItem


class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('co_nip_number',
                  'co_name',
                  'co_address',
                  'co_zip',
                  'co_city',
                  'co_country',
                  'co_telephone',
                  'co_email',
                  'co_logo')
        widgets = {'co_nip_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'co_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_address': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_zip': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_city': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_telephone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'co_email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'co_logo': forms.FileInput(attrs={'class': 'd-none cEvent'})}


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('co_nip_number',
                  'co_name',
                  'co_address',
                  'co_zip',
                  'co_city',
                  'co_country',
                  'co_telephone',
                  'co_email',
                  'co_website',
                  'co_att_person',
                  'co_payment_method',
                  'co_logo',
                  'in_currency',
                  'in_sendto_mail',
                  'in_sendto_subject',
                  'in_sendto_content',
                  'in_cc_mails',
                  'in_bcc_mails')
        widgets = {'co_nip_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'co_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_address': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_zip': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_city': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_telephone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'co_email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'co_website': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_att_person': forms.TextInput(attrs={'class': 'form-control'}),
                   'co_logo': forms.FileInput(attrs={'class': 'd-none cEvent'}),
                   'in_currency': forms.TextInput(attrs={'class': 'form-control'}),
                   'in_sendto_mail': forms.TextInput(attrs={'class': 'form-control'}),
                   'in_sendto_subject': forms.TextInput(attrs={'class': 'form-control'}),
                   'in_sendto_content': forms.Textarea(attrs={'class': 'form-control', "rows": 5, "cols": 20}),
                   'in_cc_mails': forms.TextInput(attrs={'class': 'form-control'}),
                   'in_bcc_mails': forms.TextInput(attrs={'class': 'form-control'})}


class NewInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('client',
                  'place',
                  'date_deadline',
                  'custom_comment')
        widgets = {'date_deadline': forms.TimeInput(attrs={'class': 'form-control', 'type': 'date'}),
                   'place': forms.TextInput(attrs={'class': 'form-control'}),
                   'custom_comment': forms.TextInput(attrs={'class': 'form-control'})}


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ('service',
                  'unit_price',
                  'quantity',
                  'vat_rule',
                  'unit')
        widgets = {'service': forms.TextInput(attrs={'class': 'form-control'}),
                   'unit_price': forms.TextInput(attrs={'class': 'form-control'}),
                   'quantity': forms.TextInput(attrs={'class': 'form-control'})}
