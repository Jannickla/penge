from django.shortcuts import render
from django.views.generic import FormView
from formtools.wizard.views import SessionWizardView

from .forms import FormStepOne, FormStepTwo


class Goals(SessionWizardView):
    template_name = 'dashboard/goals.html'
    form_list = [FormStepOne, FormStepTwo]

    def done(self, form_list, **kwargs):
        return render(self.request, 'dashboard/done-goal.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
