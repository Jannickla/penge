from django.urls import path
from django.contrib.auth.decorators import login_required as __

from . import views
from .apis import SalesExpensesChart
from goals.views import Goals

"""
    In this urls.py file the login_required decorator will be used on all paths. 
    This insures that the user has to be authenticated to have access to this app's urls.
    
    !!!DO NOT REMOVE OR LEAVE PATHS WITHOUT USING THIS DECORATOR UNLESS THEY'RE FBV!!!
"""

app_name = 'dashboard'

urlpatterns = [
    path('', __(views.DashboardView.as_view()), name='dashboard'),
    path('new-client/', __(views.NewClientView.as_view()), name='new-client'),
    path('client/<int:pk>', __(views.ClientView.as_view()), name='client'),
    path('edit-client/<int:pk>', __(views.UpdateClientView.as_view()), name='edit-client'),
    path('delete-client/<int:pk>',  __(views.DeleteClient.as_view()), name='delete-client'),
    path('clients/', __(views.ClientsView.as_view()), name='clients'),
    path('new-invoice/', views.new_invoice, name='new-invoice'),
    path('invoices/', __(views.InvoiceList.as_view()), name='invoice-list'),
    path('pdf/<int:invoice_id>', views.generate_pdf, name='pdf'),
    path('zus/', __(views.ZusSettlementView.as_view()), name='zus'),
    path('profile/', __(views.Profile.as_view()), name='profile'),
    path('goals/', __(Goals.as_view()), name='goals'),

    # API's
    path('api/sales-expenses', __(SalesExpensesChart.as_view()), name="sales-expenses")
]
