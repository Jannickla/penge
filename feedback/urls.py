from django.urls import path
from .views import JoinFormView

"""
    In this urls.py file the login_required decorator will be used on all paths. 
    This insures that the user has to be authenticated to have access to this app's urls.
    
    !!!DO NOT REMOVE OR LEAVE PATHS WITHOUT USING THIS DECORATOR UNLESS THEY'RE FBV!!!
"""

app_name = 'feedback'

urlpatterns = [
    path('feedback/', JoinFormView.as_view(), name="feedback"),
]
