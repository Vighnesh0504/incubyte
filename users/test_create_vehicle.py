import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_admin_can_create_vehicle():

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

    token = login.data["access"]

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        "/api/vehicles/",
        {
            "make": "Toyota",
            "model": "Corolla",
            "category": "Sedan",
            "price": 25000,
            "quantity": 5,
        },
        format="json",
    )

    assert response.status_code == 201

@pytest.mark.django_db
def test_normal_user_cannot_create_vehicle():

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

    token = login.data["access"]

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        "/api/vehicles/",
        {
            "make": "BMW",
            "model": "X5",
            "category": "SUV",
            "price": 50000,
            "quantity": 2,
        },
        format="json",
    )

    assert response.status_code == 403

@pytest.mark.django_db
def test_vehicle_price_must_be_positive():

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

    token = login.data["access"]

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )

    response = client.post(
        "/api/vehicles/",
        {
            "make": "Toyota",
            "model": "Corolla",
            "category": "Sedan",
            "price": -2000,
            "quantity": 5,
        },
        format="json",
    )

    assert response.status_code == 400

