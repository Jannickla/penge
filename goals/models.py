from django.db import models

from accounts.models import Account


class GoalsModel(models.Model):
    """
        This model contains the goals of a users company for 3 months.
    """
    # For the quarterly goal that the user aims after
    INVEST = '1'
    GROW = '2'
    TURN_AROUND = '3'
    GET_INVESTMENT = '4'

    COMPANY_GOALS = [
        (INVEST, 'Invest in new machines, development or other'),
        (GROW, 'Grow the size of employees, location or other'),
        (TURN_AROUND, 'Make a turn around to save the company'),
        (GET_INVESTMENT, 'Get Investment'),
    ]

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    quarter = models.CharField(max_length=1)
    salary = models.DecimalField(decimal_places=2, max_digits=30)
    income = models.DecimalField(decimal_places=2, max_digits=30)
    expenses = models.DecimalField(decimal_places=2, max_digits=30)
    company_goal = models.CharField(
        max_length=14,
        choices=COMPANY_GOALS,
        default=2,
    )
