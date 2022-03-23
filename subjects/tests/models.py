from django.test import TestCase
from .mockdata import subject_mockdata1, create_subject_mock, content_mockdata1, create_content_mock, keyword_mockdata1, create_keyword_mock
from ..models import Subject, Content, Keyword

# Subject Tests
class TestSubjectCase(TestCase):
    
    def setUp(self) -> None:
        create_subject_mock(subject_mockdata1)
        
    def test_if_exists(self) -> None:
        subject_count = Subject.objects.count()
        self.assertEqual(subject_count, 1)
        self.assertNotEqual(subject_count, 0)
    
    
    def test_instance(self) -> None:
        subject = Subject.objects.get(id=1)
        self.assertTrue(isinstance(subject, Subject))
    
    
    def test_create(self) -> None:
        subject = Subject.objects.get(id=1)
        name = subject.name
        self.assertEqual(name, subject_mockdata1['name'])
    
    
    def test_str(self) -> None:
        subject = Subject.objects.get(id=1)
        self.assertEqual(str(subject), subject_mockdata1['name'])
        

# Content Tests
class TestContentCase(TestCase):
    
    def setUp(self) -> None:
        create_content_mock(content_mockdata1)
    
    
    def test_if_exists(self) -> None:
        content_count = Content.objects.count()
        self.assertEqual(content_count, 1)
        self.assertNotEqual(content_count, 0)
    
    
    def test_instance(self) -> None:
        content = Content.objects.get(id=1)
        self.assertTrue(isinstance(content, Content))
    
    
    def test_create(self) -> None:
        content = Content.objects.get(id=1)
        name = content.name
        subject_id = content.subject_id.id
        url = content.url
        self.assertEqual(name, content_mockdata1['name'])
        self.assertEqual(subject_id, 1)
        self.assertEqual(url, content_mockdata1['url'])
    
    
    def test_str(self) -> None:
        content = Content.objects.get(id=1)
        self.assertEqual(str(content), content_mockdata1['name'])
    
    
    def test_url_fail(self) -> None:
        content = Content.objects.get(id=1)
        content.url= 'test/test'
        
        with self.assertRaises(ValueError):
            content.save()


# Keyword Tests
class TestKeywordCase(TestCase):
    
    def setUp(self) -> None:
        create_keyword_mock(keyword_mockdata1)
        
    
    def test_if_exists(self) -> None:
        keyword_count = Keyword.objects.count()
        self.assertEqual(keyword_count, 1)
        self.assertNotEqual(keyword_count, 0)
    
    
    def test_instance(self) -> None:
        keyword = Keyword.objects.get(id=1)
        self.assertTrue(isinstance(keyword, Keyword))
    
        
    def test_create(self) -> None:
        keyword_obj = Keyword.objects.get(id=1)
        content_id = keyword_obj.content_id.id
        keyword = keyword_obj.keyword
        self.assertEqual(content_id, 1)
        self.assertEqual(keyword, keyword_mockdata1['keyword'])
    
    
    
    def test_str(self) -> None:
        keyword_obj = Keyword.objects.get(id=1)
        self.assertEqual(str(keyword_obj), keyword_mockdata1['keyword'])
        