import pytest
from rest_framework.test import APIClient
from news_app.serializers import RegistrationSerializer


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def local_user():
    local_user = {
        'email': 'local@user.local',
        'password': '1234567890',
        'username': 'local_user',
        'first_name': 'Local',
        'last_name': 'User',
    }
    serializer = RegistrationSerializer(data=local_user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return local_user