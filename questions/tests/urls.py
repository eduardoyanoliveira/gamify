from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from util.tests.global_setup import GlobalTestSetUp
from .mockdata import question_mockdata1, create_question_mock, answer_mockdata1, create_answer_mock


class TestQuestionViewCase(GlobalTestSetUp, APITestCase):
    
    url = '/api/questions/'
    
    def setUp(self) -> None:
        super().setUp()


    def test_view(self) -> None:
        response = self.client.get(TestQuestionViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        question = create_question_mock(question_mockdata1)

        data = {
            "name" : question.name,
            "text" : question.text,
            "author" : question.author.id,
            "difficulty_id": question.difficulty_id.id,
            "likes": [1]
        }

        response = self.client.post(TestQuestionViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        create_question_mock(question_mockdata1)
        response = self.client.delete(TestQuestionViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
    


  

class TestAnswerViewCase(GlobalTestSetUp, APITestCase):
    
    url = '/api/answers/'
   
    def setUp(self) -> None:
        super().setUp()

    
    def test_view(self) -> None:
        response = self.client.get(TestAnswerViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        answer = create_answer_mock(answer_mockdata1)
        
        data = {
            "name": answer.name,
            "text": answer.text,
            "author": answer.author.id,
            "question_id": answer.question_id.id,
            "likes": [1]
        }
        
        response = self.client.post(TestAnswerViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    
    def test_delete_view(self) -> None:
        create_answer_mock(answer_mockdata1)
        response = self.client.delete(TestAnswerViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])