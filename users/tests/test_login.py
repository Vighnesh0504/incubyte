import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.mark.django_db
def test_login_returns_valid_jwt():

    User.objects.create_user(
        username="john",
        password="Password@123"
    )

    client = APIClient()

    response = client.post(
        "/api/auth/login/",
        {
            "username": "john",
            "password": "Password@123"
        },
        format="json"
    )

    assert response.status_code == 200

    assert len(response.data["access"]) > 20

    assert len(response.data["refresh"]) > 20