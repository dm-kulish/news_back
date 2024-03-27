import pytest


class TestAPIAuthRegister:
    """Testing /api/auth/register/ api."""

    API_PATH = '/api/auth/register/'

    def test_allowed_methods_request(self, client):
        response = client.get(self.API_PATH)
        assert response.status_code == 405

        allowed_headers = response.headers['Allow'].split(', ')
        if all(method in allowed_headers for method in ['POST', 'OPTIONS']):
            assert True
        else:
            assert False

    @pytest.mark.django_db
    def test_user_registration(self, client):
        test_user = {
            # required fields
            'email': 'test@test.test',
            'password': '1234567890',
            'username': 'test_user',
            # optional fields
            'first_name': 'Ta',
            'last_name': 'Tb',
            'image': '',
        }
        response = client.post(self.API_PATH, test_user)
        assert response.status_code == 201

        assert not ('password' in response.data['User'])
