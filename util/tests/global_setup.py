from django.test import TestCase
from accounts.tests.mockdata import user_mockdata1, user_mockdata2, create_user_mock

class GlobalTestSetUp(TestCase):
    
    def setUp(self) -> None:
        create_user_mock(user_mockdata1)
        create_user_mock(user_mockdata2)