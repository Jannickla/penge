from rest_framework import serializers
from .models import Invoice, ExpensesToPay, ExpensesPaid


class InvoiceSer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('total',)


class ExpensesPaidSer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesPaid
        fields = ('price',)


class ExpensesToPaySer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesToPay
        fields = ('price',)
