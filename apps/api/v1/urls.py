from django.urls import path

from apps.api.v1.auth.users import UserView
from apps.api.v1.auth.views import AuthView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),

]
