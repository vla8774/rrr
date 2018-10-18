
from django.conf.urls import url
from . import views

urlpatterns = \
[
    url(r"^signin/$", views.signin, name = "signin"),
    url(r"^do_signin/$", views.do_signin, name = "do_signin"),
    url(r"^signup/$", views.signup, name = "signup"),
    url(r"^do_signup/$", views.do_signup, name = "do_signup"),
    url(r"^signup_done/$", views.signup_done, name = "signup_done"),
]

