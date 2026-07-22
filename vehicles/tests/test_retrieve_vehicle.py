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

@pytest.mark.django_db
def test_admin_can_update_vehicle():

    vehicle = Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )

    admin = User.objects.create_user(
        username="admin",
        password="Password@123",
        is_staff=True,
    )

    client = APIClient()

    login = client.post(
        "/api/auth/login/",
        {
            "username": "admin",
            "password": "Password@123",
        },
        format="json",
    )

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {login.data['access']}"
    )

    response = client.put(
        f"/api/vehicles/{vehicle.id}/",
        {
            "make": "Toyota",
            "model": "Camry",
            "category": "Sedan",
            "price": 32000,
            "quantity": 10,
        },
        format="json",
    )

    assert response.status_code == 200

    vehicle.refresh_from_db()

    assert vehicle.model == "Camry"

@pytest.mark.django_db
def test_normal_user_cannot_update_vehicle():

    vehicle = Vehicle.objects.create(
        make="BMW",
        model="X5",
        category="SUV",
        price=60000,
        quantity=3,
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

    response = client.put(
        f"/api/vehicles/{vehicle.id}/",
        {
            "make": "BMW",
            "model": "X6",
            "category": "SUV",
            "price": 65000,
            "quantity": 3,
        },
        format="json",
    )

    assert response.status_code == 403

@pytest.mark.django_db
def test_admin_can_delete_vehicle():

    vehicle = Vehicle.objects.create(
        make="Audi",
        model="A4",
        category="Sedan",
        price=50000,
        quantity=2,
    )

    admin = User.objects.create_user(
        username="admin",
        password="Password@123",
        is_staff=True,
    )

    client = APIClient()

    login = client.post(
        "/api/auth/login/",
        {
            "username": "admin",
            "password": "Password@123",
        },
        format="json",
    )

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {login.data['access']}"
    )

    response = client.delete(f"/api/vehicles/{vehicle.id}/")

    assert response.status_code == 204

    assert Vehicle.objects.count() == 0