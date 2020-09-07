from django.views import View
from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from djstripe.models import Product

from blog.models import Post
from .forms import ContactForm


class HomeView(TemplateView):
    template_name = 'website/index.html'


class BlogView(ListView):
    template_name = 'website/blog.html'
    model = Post
    paginate_by = 4


class ContactView(FormView):
    template_name = 'website/contact.html'
    form = ContactForm
    success_url = ''

    def form_valid(self, *args, form):
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')

    def get(self, request, *args):
        return render(request, self.template_name, {'form': self.form})


class BlogDetailView(DetailView):
    template_name = 'website/blog-details.html'
    model = Post
    pk_url_kwarg = 'id'


class PricingView(View):
    template_name = 'website/pricing.html'

    def get(self, request, *args, **kwargs):
        # Get all Pricing models in our DB
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class FeaturesView(TemplateView):
    template_name = 'website/features.html'


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset
    }

    return render(request, 'website/results.html', context)
