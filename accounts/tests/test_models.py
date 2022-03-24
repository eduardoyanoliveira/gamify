from ..models import CustomUser
from .test_mockdata import user_mockdata1, user_mockdata2
from util.tests.global_setup import GlobalTestSetUp

class TestUserCase(GlobalTestSetUp):
    
    def setUp(self) -> None:
        super().setUp()


    def test_create(self) -> None:
        user = CustomUser.objects.get(id=1)
        user_name = user.user_name
        email = user.email
        xp = user.xp
        cash = user.cash
        password = user.password
        
        self.assertEqual(user_name,user_mockdata1['user_name'])
        self.assertEqual(email,user_mockdata1['email'])
        self.assertEqual(xp, user_mockdata1['xp'])
        self.assertEqual(cash, user_mockdata1['cash'])
        self.assertEqual(password, user_mockdata1['password'])
    
    
    def test_str(self) -> None:
        user = CustomUser.objects.get(id=2)
        self.assertEqual(str(user), user_mockdata2['user_name'])
    
    
    def test_is_staff(self) -> None:
        user = CustomUser.objects.get(id=2)
        self.assertFalse(user.is_staff)
        
    
    def test_xp_error(self) -> None:
        user = CustomUser.objects.get(id=2)
        user.xp = -70
        
        with self.assertRaises(ValueError):
            user.save()
        
    
    def test_cash_error(self) -> None:
        user = CustomUser.objects.get(id=2)
        user.cash = -500
        
        with self.assertRaises(ValueError):
            user.save()
    
    
    def test_password_error(self) -> None:
        user = CustomUser.objects.get(id=2)
        user.password = 'test'
        
        with self.assertRaises(ValueError):
            user.save()