from feedback.forms import FeedbackForm
from marketing.forms import EmailSignupForm


def feedback_form(request):

    return {
         'feedback_form': FeedbackForm()
    }


def email_subscription_form(request):

    return {
         'email_subscription_form': EmailSignupForm()
    }
