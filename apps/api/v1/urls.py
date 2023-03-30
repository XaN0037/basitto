from django.urls import path

from apps.api.v1.auth.users import UserView
from apps.api.v1.auth.views import AuthView
from apps.dashboard.v1.basket.views import BasketView
from apps.dashboard.v1.category.views import SubCategoryView
from apps.dashboard.v1.product.views import ProductView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),

    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductView.as_view()),

    path("subcategory/", SubCategoryView.as_view()),
    path("subcategory/<int:pk>/", SubCategoryView.as_view()),

path("basket/", BasketView.as_view()),
    path("basket/<int:pk>/", BasketView.as_view()),

]
