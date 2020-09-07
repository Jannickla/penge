from django.contrib import admin
from .models import *


class Contact(admin.ModelAdmin):
    list_display = ('user',
                    'co_nip_number',
                    'co_name',
                    'co_address',
                    'co_zip',
                    'co_city',
                    'co_country',
                    'co_telephone',
                    'co_email',
                    'co_website',
                    'co_att_person',
                    'co_ean_number',
                    'co_payment_method')


admin.site.register(Client, Contact)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(ExpensesPaid)
admin.site.register(ExpensesToPay)
