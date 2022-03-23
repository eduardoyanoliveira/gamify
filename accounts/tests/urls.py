from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import CustomUser
from util.tests.global_setup import GlobalTestSetUp


class TestUserViewCase(GlobalTestSetUp, APITestCase):
    
    url = '/accounts/users/'
    
    def setUp(self) -> None:
        super().setUp()
    
    
    def test_view(self) -> None:
        response = self.client.get(TestUserViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        
        user = CustomUser.objects.get(id=1)

        data = {
            "user_name" : 'Another',
            "email": 'another@another.com',
            "xp": user.xp,
            "cash": user.cash,
            "password": user.password
        }

        response = self.client.post(TestUserViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        response = self.client.delete(TestUserViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
