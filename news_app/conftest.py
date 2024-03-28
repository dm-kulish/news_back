import pytest
from rest_framework.test import APIClient
from news_app.serializers import UserSerializer


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def local_user():
    local_user = {
        'email': 'local@user.local',
        'password': 'Django_test555',
        'username': 'local_user',
        # 'first_name': 'Local',
        # 'last_name': 'User',
    }
    serializer = UserSerializer(data=local_user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return local_user
