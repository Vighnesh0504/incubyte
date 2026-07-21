import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user():

    client = APIClient()

    response = client.post(
        "/api/auth/register/",
        {
            "username": "john",
            "email": "john@gmail.com",
            "password": "Password@123",
        },
        format="json",
    )

    assert response.status_code == 201

    assert User.objects.filter(username="john").exists()