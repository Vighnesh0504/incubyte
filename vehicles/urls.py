from django.urls import path

from .views import VehicleCreateView

urlpatterns = [
    path(
        "",
        VehicleCreateView.as_view(),
        name="create-vehicle",
    ),
]