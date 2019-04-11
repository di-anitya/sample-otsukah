from django.urls import path

from . import views

# set the application namespace
app_name = 'accounts'

urlpatterns = [
    # ex: /accounts/signup/
    path('signup/', views.SignUpView.as_view(), name='signup')
]
