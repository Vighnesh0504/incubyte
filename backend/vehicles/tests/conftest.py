import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def admin_client():

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

    return client


@pytest.fixture
def user_client():

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

    return client