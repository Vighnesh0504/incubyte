from django.urls import path

from .views import (
    VehicleDetailView,
    VehicleListCreateView,
    VehicleSearchView,
    PurchaseVehicleView,
    RestockVehicleView
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
    path(
    "<int:pk>/purchase/",
    PurchaseVehicleView.as_view(),
    ),
    path(
        "<int:pk>/restock/",
        RestockVehicleView.as_view(),
    ),
]