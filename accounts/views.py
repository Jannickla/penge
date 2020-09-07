from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView, RedirectView

from .forms import RegistrationForm, AccountAuthenticationForm
from .models import Account


class LoginView(FormView):
    """
    Provides the ability to login as a user with a e-mail and password
    """
    template_name = 'website/login.html'
    success_url = '/dashboard/'
    form_class = AccountAuthenticationForm

    def form_valid(self, form):
        email = self.request.POST['email']
        password = self.request.POST['password']
        user = authenticate(email=email, password=password)

        if user:
            auth_login(self.request, user)
            return redirect('dashboard:dashboard')


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegistrationView(FormView):
    """
    Registration with e-mail confirmation.
    We're here using get_current_site, which belongs on
    the defined site in django admin.

    Use request.get_host() not to belong on admin values.
    """
    template_name = 'website/register.html'
    form_class = RegistrationForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Send activation E-mail
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your Penge account.'
        message = render_to_string('emails/activation-mail.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to activate your Penge account')


def activate(request, uidb64, token):
    """
    E-mail activation for user registration.
    Strongly recommended not to remove this!

    This is validating the token sent by our RegistrationView above.
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
