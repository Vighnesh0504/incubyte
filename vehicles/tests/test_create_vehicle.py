import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


# -------------------------------------------------------------------
# Pytest Fixtures for Clean, Reusable Setup
# -------------------------------------------------------------------

@pytest.fixture
def admin_user(db):
    """Creates and returns a staff/admin user."""
    return User.objects.create_user(
        username="admin",
        password="Password@123",
        is_staff=True,
    )


@pytest.fixture
def normal_user(db):
    """Creates and returns a non-staff user."""
    return User.objects.create_user(
        username="john",
        password="Password@123",
    )


def get_authenticated_client(username, password="Password@123"):
    """Helper function to log in a user and return an authenticated APIClient."""
    client = APIClient()
    login_res = client.post(
        "/api/auth/login/",
        {"username": username, "password": password},
        format="json",
    )
    token = login_res.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client


@pytest.fixture
def admin_client(admin_user):
    """Returns an APIClient authenticated as an admin user."""
    return get_authenticated_client(admin_user.username)


@pytest.fixture
def user_client(normal_user):
    """Returns an APIClient authenticated as a normal user."""
    return get_authenticated_client(normal_user.username)


# -------------------------------------------------------------------
# Clean Test Cases
# -------------------------------------------------------------------

@pytest.mark.django_db
def test_admin_can_create_vehicle(admin_client):
    response = admin_client.post(
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
    assert response.data["make"] == "Toyota"


@pytest.mark.django_db
def test_normal_user_cannot_create_vehicle(user_client):
    response = user_client.post(
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
def test_vehicle_price_must_be_positive(admin_client):
    response = admin_client.post(
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
    assert "price" in response.data