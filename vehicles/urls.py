from django.urls import path

from .views import (
    VehicleDetailView,
    VehicleListCreateView,
    VehicleSearchView
)

urlpatterns = [

    path(
        "",
        VehicleListCreateView.as_view(),
    ),

    path(
        "<int:pk>/",
        VehicleDetailView.as_view(),
    ),
    path(
        "search/",
        VehicleSearchView.as_view(),
    ),

]