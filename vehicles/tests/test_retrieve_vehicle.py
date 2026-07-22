import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient

from vehicles.models import Vehicle


@pytest.mark.django_db
def test_authenticated_user_can_get_vehicle():

    vehicle = Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=4,
    )

    user = User.objects.create_user(
        username="john",
        password="Password@123",
    )

    client = APIClient()

    login = client.post(
        "/api/auth/login/",
        {
            "username": "john",
            "password": "Password@123",
        },
        format="json",
    )

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {login.data['access']}"
    )

    response = client.get(f"/api/vehicles/{vehicle.id}/")

    assert response.status_code == 200

    assert response.data["make"] == "Toyota"