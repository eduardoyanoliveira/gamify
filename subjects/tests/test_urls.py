from rest_framework.test import APITestCase
from rest_framework import status

from subjects.models import Content, Keyword, Subject

from .test_mockdata import subject_mockdata1, create_subject_mock
from .test_mockdata import content_mockdata1, create_content_mock
from .test_mockdata import keyword_mockdata1, create_keyword_mock

from accounts.tests.test_mockdata import super_mockdata, create_super_mock


class TestSubjectViewCase(APITestCase):
    
    url = '/api/subjects/'
    
    def setUp(self) -> None:
        create_super_mock(super_mockdata)
        
        self.user_name= super_mockdata['user_name']
        self.password = super_mockdata['password']
        
        create_subject_mock(subject_mockdata1)


    def test_view(self) -> None:
        response = self.client.get(TestSubjectViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_fail_no_auth(self) -> None:
        """
        Must be a super user
        """
        subject = Subject.objects.get(id=1)

        data = {
            "name" : subject.name,
        }

        response = self.client.post(TestSubjectViewCase.url, data, format='json')
        self.assertTrue(response.status_code in [status.HTTP_403_FORBIDDEN, status.HTTP_401_UNAUTHORIZED])


    def test_create_view(self) -> None:
        
        self.client.login(user_name=self.user_name, password=self.password)
        
        subject = Subject.objects.get(id=1)

        data = {
            "name" : subject.name,
        }

        response = self.client.post(TestSubjectViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        
        self.client.login(user_name=self.user_name, password=self.password)
        
        response = self.client.delete(TestSubjectViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])


class TestContentViewCase(APITestCase):
    
    url = '/api/contents/'
    
    def setUp(self) -> None:
        create_content_mock(content_mockdata1)
    
    
    def test_view(self) -> None:
        response = self.client.get(TestContentViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        
        content = Content.objects.get(id=1)

        data = {
            "name" : content.name,
            "subject_id": content.subject_id.id,
            "url": 'https://www.youtube.com/watch?v=Y4R6k8_iIkE'
        }

        response = self.client.post(TestContentViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        response = self.client.delete(TestContentViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
               

class TestKeywordViewCase(APITestCase):
    
    url = '/api/keywords/'
    
    def setUp(self) -> None:
        create_keyword_mock(keyword_mockdata1)
    
    
    def test_view(self) -> None:
        response = self.client.get(TestKeywordViewCase.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_create_view(self) -> None:
        
        keyword = Keyword.objects.get(id=1)

        data = {
            "keyword" : keyword.keyword,
            "content_id": keyword.content_id.id,
        }

        response = self.client.post(TestKeywordViewCase.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_delete_view(self) -> None:
        response = self.client.delete(TestKeywordViewCase.url + '1/', content_type='application/json')
        self.assertTrue(response.status_code in [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])
        