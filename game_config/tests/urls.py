from rest_framework import status
from rest_framework.test import APITestCase
from util.tests.global_setup import GlobalTestSetUp
from .mockdata import user_level_mockdata1, difficulty_mockdata1, create_difficulty_mock, create_user_level_mock


class TestUserLevelViewCase(GlobalTestSetUp, APITestCase):
    
    url = '/api/levels/'
    
    def setUp(self) -> None:
        super().setUp()
    
    
    def test_view(self) -> None:
        response = self.client.get(TestUserLevelViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        
        user_level = create_user_level_mock(user_level_mockdata1)

        data = {
            "name" : user_level.name,
            "pts" : user_level.pts,
        }

        response = self.client.post(TestUserLevelViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        create_user_level_mock(user_level_mockdata1)
        response = self.client.delete(TestUserLevelViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])


class TestDifficultyViewCase(GlobalTestSetUp, APITestCase):
    
    url = '/api/difficulties/'
    
    def setUp(self) -> None:
        super().setUp()
    
    
    def test_view(self) -> None:
        response = self.client.get(TestDifficultyViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        
        difficulty = create_difficulty_mock(difficulty_mockdata1)

        data = {
            "name" : difficulty.name,
            "color" :  difficulty.color,
            "pts" : difficulty.pts,
        }

        response = self.client.post(TestDifficultyViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        create_difficulty_mock(difficulty_mockdata1)
        response = self.client.delete(TestDifficultyViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
        