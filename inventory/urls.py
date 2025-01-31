from django.urls import path

from .views import (
    HomeView,
    ProductListView,
    ProductInputView,
    ShowStringView,
    ShowDetailsProductView,
)


urlpatterns = [
    path("", HomeView.as_view(), name='index'),
    path("add/", ProductInputView.as_view(), name='add_product'),
    path("information/", ProductListView.as_view(), name='info_product'),
    path("username/<str:query_string>", ShowStringView.as_view(), name='show_string'),
    path("<int:query_id>/", ShowDetailsProductView.as_view(), name='show_product_detail'),
]
