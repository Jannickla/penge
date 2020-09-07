from django.urls import path
from blog.views import SearchView, PostListView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('search/', SearchView.as_view(), name="blog-search"),
    path('blog/', PostListView.as_view(), name="blog"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-details")
]
