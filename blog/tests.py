import pytest
from django.test import TestCase
from rest_framework.test import force_authenticate, APIRequestFactory, APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestOne:
    def test_one(self):
        client = APIClient()
        client.force_authenticate()

        # Make an authenticated request to the view...
        response = client.get('/router/tests/')
        force_authenticate(response.data)
        print(response.data)
        assert response.data == []