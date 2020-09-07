from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.http import JsonResponse
from django.core import serializers

from .forms import FeedbackForm


class JoinFormView(FormView):
    form_class = FeedbackForm
    template_name = 'dashboard/base.html'
    success_url = '/'

    def form_invalid(self, form):
        response = super(JoinFormView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(JoinFormView, self).form_valid(form)
        if self.request.is_ajax():
            instance = form.save(commit=False)

            if self.request.POST.get('button') == 1:
                instance.overall_satisfaction = 1
            elif self.request.POST.get('button') == 2:
                instance.overall_satisfaction = 2
            elif self.request.POST.get('button') == 3:
                instance.overall_satisfaction = 3
            elif self.request.POST.get('button') == 4:
                instance.overall_satisfaction = 4
            elif self.request.POST.get('button') == 5:
                instance.overall_satisfaction = 5
            else:
                instance.overall_satisfaction = 0  # Nothing chosen

            print('self.request.POST')
            print(self.request.POST)

            instance.user = self.request.user
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            print(form.cleaned_data)
            data = {
                'message': 'Successfully submitted form data.',
                'instance': ser_instance
            }
            return JsonResponse(data, status=200)
        else:
            return response


# def feedback_form(request):
#     fb_form = FeedbackForm()
#     # Figure which satisfaction button is chosen and set the value
#     if request.POST and request.is_ajax:
#         fb_form = FeedbackForm(request.POST)
#         if fb_form.is_valid():
#             fb_form.user = request.user
#             if request.POST['button'] == '1':
#                 fb_form.overall_satisfaction = 1
#             elif request.POST['button'] == '2':
#                 fb_form.overall_satisfaction = 2
#             elif request.POST['button'] == '3':
#                 fb_form.overall_satisfaction = 3
#             elif request.POST['button'] == '4':
#                 fb_form.overall_satisfaction = 4
#             elif request.POST['button'] == '5':
#                 fb_form.overall_satisfaction = 5
#             else:
#                 fb_form.overall_satisfaction = 0  # Nothing chosen
#
#             fb_form.save()
#
#             return redirect('dashboard:dashboard')
#     else:
#
#         return {'fb_form': fb_form}
