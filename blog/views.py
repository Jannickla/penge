from django.db.models import Count, Q
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView

from .forms import CommentForm
from .models import Post, Author, PostView
from marketing.forms import EmailSignupForm

form = EmailSignupForm()


class SearchView(View):
    def get(self, request, *args, **kwargs):
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


class PostListView(ListView):
    model = Post
    template_name = 'website/blog.html'
    context_object_name = 'queryset'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'website/blog-details.html'
    context_object_name = 'post'
    form = CommentForm()

    def get_object(self):
        obj = super().get_object()

        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(
                user=self.request.user,
                post=obj
            )

        return obj

    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        most_recent = Post.objects.order_by('-timestamp')[:3]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['page_request_var'] = "page"
        context['category_count'] = category_count
        context['form'] = self.form

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("blog:blog-details", kwargs={
                'pk': post.pk
            }))


def get_author(user):
    qs = Author.objects.filter(user=user)

    if qs.exists():
        return qs[0]

    return None


def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))

    return queryset
