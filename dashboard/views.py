from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DeleteView, DetailView, UpdateView
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Max, Sum
from django.forms import inlineformset_factory
from django.template.loader import render_to_string
from django.db.models.functions import datetime
from django.utils import translation

from weasyprint import HTML
from datetime import date
from decimal import Decimal

import tempfile

from .forms import NewClientForm, NewInvoiceForm, UpdateClientForm
from .models import Client, InvoiceItem, Invoice, ExpensesToPay, ExpensesPaid
from accounts.models import Account

from accounts.forms import AccountEditForm


class DashboardView(DetailView):
    """
    The overview and the dashboard of a logged in user
    """
    template_name = 'dashboard/index.html'
    model = Account

    def get(self, request, *args, **kwargs):
        user = Account.objects.get(email=request.user)  # Set the user

        # Get the years of activity for the top chart
        # years = set()
        # for invoice in user.invoice.all():
        #     years.add(invoice.created_at.year)
        #     total = 0
        #     for item in invoice.items.all():
        #         result = Decimal(item.vat_rule)
        #         total += item.unit_price * item.quantity * (1 + result / 100)
        #     overall_item_total = round(total, 2)

        # Get the total income
        total_income = 0
        for i in user.invoice.all():
            for item in i.items.all():
                result = Decimal(item.vat_rule)
                total_income += item.unit_price * item.quantity * (1 + result / 100)
        sum_income = round(total_income, 2)
        # print(sum_income)

        # Get the total expenses
        total_paid = ExpensesPaid.objects.all().aggregate(Sum('price'))['price__sum'] or 0.00
        total_to_pay = ExpensesToPay.objects.all().aggregate(Sum('price'))['price__sum'] or 0.00
        sum_expenses = Decimal(total_paid) + Decimal(total_to_pay)
        # print(sum_expenses)

        # Expenses subtracted from Income
        total_earning = sum_income - sum_expenses

        # Check if the income is as expected in current year
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year
        last_day_of_year = date(current_year, 12, 31)
        month_left = 12 - int(current_month)
        current_goal = 5000  # TODO: Make the client able to choose the goal
        goal_share = current_goal / 12

        if int(total_income) >= goal_share * int(current_month):
            business_status = 'Your business goes well'
        else:
            business_status = "Your business doesn't go well"
        print(month_left)
        print(current_year)

        # Clients count
        clients_amount = user.clients.count()

        context = {
            # 'years': years,
            'sum_income': sum_income,
            'sum_expenses': sum_expenses,
            'total_earning': total_earning,
            'business_status': business_status,
            'clients_amount': clients_amount
        }

        return render(request, template_name=self.template_name, context=context)


class Profile(UpdateView):
    """
    The users profile
    """
    template_name = 'dashboard/profile.html'
    form_class = AccountEditForm
    success_url = '/dashboard/profile'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def post(self, request, **kwargs):
        if request.user.is_authenticated:
            translation.activate(request.user.language)
        return super(Profile, self).post(request, **kwargs)


class ClientView(ListView):
    """
    A Overview over a single clients details
    """
    model = Client
    ordering = ['-created_on']
    paginate_by = 10
    template_name = 'dashboard/client.html'

    def get_context_data(self, *args, **kwargs):
        client = Client.objects.get(pk=self.kwargs['pk'])
        context = {
            'client': client
        }

        return context


class UpdateClientView(UpdateView):
    """
    Update client details
    """
    form_class = UpdateClientForm
    model = Client
    template_name = 'dashboard/client-settings.html'
    success_url = 'dashboard/client-settings.html'


class ClientsView(ListView):
    """
    A list over clients
    """
    model = Client
    template_name = 'dashboard/clients.html'


class NewClientView(FormView):
    """
    A form to create new clients
    """
    form_class = NewClientForm
    template_name = 'dashboard/new-client.html'
    success_message = "Client was created successfully."

    def form_valid(self, form):
        # Getting the user who created the client
        contact = form.save(commit=False)
        contact.user = self.request.user
        contact.save()
        messages.success(self.request, self.success_message)

        return redirect('dashboard:clients')


class DeleteClient(DeleteView):
    """
    A view for deleting clients with AJAX at dashboard:clients
    """
    model = Client
    success_url = reverse_lazy('dashboard:clients')
    success_message = "Client was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteClient, self).delete(request, *args, **kwargs)


def new_invoice(request):
    """
    A form to create and send an invoice to your clients
    """
    # Formset for items on the invoice (Services)
    invoice_formset = inlineformset_factory(
        Invoice,
        InvoiceItem,
        fields=('service',
                'unit_price',
                'quantity',
                'vat_rule',
                'unit'),
        can_delete=True
    )

    # Creating the invoice
    if request.method == 'POST':
        invoice_form = NewInvoiceForm(request.POST)
        if invoice_form.is_valid():
            invoice = invoice_form.save(commit=False)
            invoice.user = request.user  # Getting the user who created the invoice
            max_invoice_id = Invoice.objects.filter(user=request.user).aggregate(max_id=Max('invoice_id'))['max_id']
            if max_invoice_id:
                # check if it's not None (verify what returns aggregate() on empty queryset, adjust accordingly
                invoice.invoice_id = max_invoice_id + 1
            else:
                invoice.invoice_id = 1
            invoice.save()
            formset = invoice_formset(request.POST, instance=invoice)
            if formset.is_valid():
                formset.save(commit=False)
                total = 0
                for i in formset:
                    quantity = i.cleaned_data['quantity']
                    price = i.cleaned_data['unit_price']
                    vat = Decimal(i.cleaned_data['vat_rule'])
                    total += price * quantity * (1 + vat / 100)

                overall_invoice_total = round(total, 2)
                print(overall_invoice_total)
                invoice.total = overall_invoice_total
                invoice.save()
                formset.save()

                messages.success(request, "Invoice created.")

                return redirect('dashboard:dashboard')
        else:
            formset = invoice_formset()
            invoice_form = NewInvoiceForm()
    else:
        formset = invoice_formset()
        invoice_form = NewInvoiceForm()

    context = {
        'invoice_form': invoice_form,
        'formset': formset,
        'invoice': Invoice,
        'time': date,
        'city': Account.objects.only('co_city'),
        'pk': request.user.pk
    }
    return render(request, 'dashboard/new-invoice.html', context)


def generate_pdf(request, invoice_id):
    """
    Generate pdf using weasyprint
    """
    # Model data
    invoice = Invoice.objects.get(pk=invoice_id, user=request.user)
    client = Client.objects.all()
    invoice_items = invoice.items.all()

    # Gets the total price on the whole invoice and instance it to Invoice.total field
    total = 0
    for item in invoice_items:
        result = Decimal(item.vat_rule)
        total += item.unit_price * item.quantity * (1 + result / 100)

    overall_invoice_total = round(total, 2)
    Invoice.objects.create(total=overall_invoice_total)

    context = {
        'client': client,
        'invoice': invoice,
        'invoice_items': invoice_items,
        'total': overall_invoice_total
    }

    # Rendered
    html_string = render_to_string('emails/invoice.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')  # rb for 'Read Binary'
        response.write(output.read())

    return response


class ZusSettlementView(TemplateView):
    """
        A guide to fill out ZUS applications
    """
    template_name = 'dashboard/zus-settlement.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'page_title': 'ZUS'
        }

        return context


class InvoiceList(ListView):
    """
        A list over Invoices sent
    """
    template_name = 'dashboard/invoice-list.html'
    model = Invoice
