from . import views
from django.urls import path


urlpatterns = [
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-out/", views.SignOutView.as_view(), name="sign-out"),
]
