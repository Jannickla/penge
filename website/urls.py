from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomeView.as_view(), name="w-home-view"),
    path('contact/', views.ContactView.as_view(), name="w-contact-view"),
    path('blog/', views.BlogView.as_view(), name="w-blog-view"),
    path('blog/results/', views.search, name="w-blog-results-view"),
    path('post/<id>/', views.BlogDetailView.as_view(), name="w-blog-details-view"),
    path('features/', views.FeaturesView.as_view(), name="w-features-view"),
    path('pricing', views.PricingView.as_view(), name="w-pricing-view")
]
