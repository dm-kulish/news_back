import pytest


class TestAPIAuthLoginToken:

    API_PATH = '/token/login/'

    def test_allowed_methods_request(self, client):
        response = client.get(self.API_PATH)
        assert response.status_code == 405

        allowed_headers = response.headers['Allow'].split(', ')
        assert all(method in allowed_headers for method in ['POST', 'OPTIONS'])

    @pytest.mark.django_db
    def test_user_identification(self, client, local_user):
        request_data = {
            'email': local_user['email'],
            'password': local_user['password'],
        }
        response = client.post(self.API_PATH, request_data)
        assert response.status_code == 200

        assert 'refresh' in response.data and 'access' in response.data
