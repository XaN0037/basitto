from django.urls import path

from apps.api.v1.auth.users import UserView
from apps.api.v1.auth.views import AuthView
from apps.dashboard.v1.banner.views import BannerViews
from apps.dashboard.v1.basket.views import BasketView
from apps.dashboard.v1.category.views import SubCategoryView
from apps.dashboard.v1.discount.views import DiscountView
from apps.dashboard.v1.product.views import ProductView
from apps.dashboard.v1.comments.views import CommentView, Comments
from apps.dashboard.v1.prosaved.views import ProsavedView

urlpatterns = [
    path("auth/", AuthView.as_view()),
    path("user/", UserView.as_view()),

    path("product/", ProductView.as_view()),
    path("product/<int:pk>/", ProductView.as_view()),

    path("subcategory/", SubCategoryView.as_view()),
    path("subcategory/<int:pk>/", SubCategoryView.as_view()),

    path("basket/", BasketView.as_view()),
    path("basket/<int:pk>/", BasketView.as_view()),


    path("discount/<int:pk>/", DiscountView.as_view()),
    path("discount/", DiscountView.as_view()),

    path("comments/", CommentView.as_view()),
    path("comments/<int:pk>/", Comments.as_view()),

    path("banner/<int:pk>/", BannerViews.as_view()),
    path("banner/", BannerViews.as_view()),

    path("prosaved/", ProsavedView.as_view()),

]

