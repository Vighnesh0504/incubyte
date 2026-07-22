import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from vehicles.models import Vehicle


# -------------------------------------------------------------------
# Pytest Fixtures
# -------------------------------------------------------------------

@pytest.fixture
def normal_user(db):
    """Creates and returns a standard authenticated user."""
    return User.objects.create_user(
        username="john",
        password="Password@123",
    )


@pytest.fixture
def user_client(normal_user):
    """Returns an APIClient authenticated with a JWT token for normal_user."""
    client = APIClient()
    login_res = client.post(
        "/api/auth/login/",
        {"username": normal_user.username, "password": "Password@123"},
        format="json",
    )
    token = login_res.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client


# -------------------------------------------------------------------
# Test Cases
# -------------------------------------------------------------------

@pytest.mark.django_db
def test_authenticated_user_can_list_vehicles(user_client):
    # Setup vehicle records in the test database
    Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )
    Vehicle.objects.create(
        make="BMW",
        model="X5",
        category="SUV",
        price=70000,
        quantity=2,
    )

    response = user_client.get("/api/vehicles/")

    assert response.status_code == 200
    # Access "results" key due to DRF pagination wrapping
    assert len(response.data["results"]) == 2
    assert response.data["count"] == 2


@pytest.mark.django_db
def test_anonymous_user_cannot_list_vehicles():
    client = APIClient()

    response = client.get("/api/vehicles/")

    assert response.status_code == 401