from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Account


class SalesExpensesChart(APIView):
    """
    View to list all sales and expenses.

    * Requires session authentication.
    * Only the users own data is visible to the user authenticated.
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        # Variables for object calls
        user = Account.objects.get(email=request.user)
        invoices = user.invoice.all()
        expenses_to_pay = user.expenses_to_pay.all()
        expenses_paid = user.expenses_paid.all()

        # Set all months to 0 - This is done to show them at the right label
        total_earn_month = {}
        total_etp_month = {}
        total_ep_month = {}
        for month in range(0, 12):
            total_earn_month[month] = 0
            total_etp_month[month] = 0
            total_ep_month[month] = 0

        # Get total earnings in the different months (month: 1-12)
        for invoice in invoices:
            invoice_month = invoice.created_at.month
            total_earn_month[invoice_month-1] += invoice.total

        # Get total expenses to pay in the different months (month: 1-12)
        for expense in expenses_to_pay:
            etp_month = expense.invoice_date.month
            total_etp_month[etp_month-1] += expense.price

        # Get total expenses to pay in the different months (month: 1-12)
        for expense in expenses_paid:
            ep_month = expense.purchase_date.month
            total_ep_month[ep_month-1] += expense.price

        # add the two dicts for the two different expenses to one dict
        total_expenses = {k: total_ep_month.get(k, 0) + total_etp_month.get(k, 0)
                          for k in set(total_ep_month.keys()) | set(total_etp_month.keys())}

        # Get labels
        labels = ['January',
                  'February',
                  'March',
                  'April',
                  'May',
                  'June',
                  'July',
                  'August',
                  'September',
                  'October',
                  'November',
                  'December']

        # Pack values to pass them to the template
        sales = total_earn_month.values()
        print(total_ep_month)

        return Response({
            'labels': labels,
            'sales': sales,
            'total_expenses': total_expenses.values()
        })
