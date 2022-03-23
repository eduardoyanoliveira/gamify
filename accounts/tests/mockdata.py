from ..models import CustomUser

user_mockdata1 = {
    "user_name": 'test_user',
    "email": 'test@test.com',
    "xp": 737,
    "cash": 315,
    "password": 'test21'
}

user_mockdata2 = {
    "user_name": 'test_user2',
    "email": 'test2@test2.com',
    "xp": 517,
    "cash": 505,
    "password": 'test25'
}

def create_user_mock(user_mockdata) -> CustomUser:
    return CustomUser.objects.create(
        user_name= user_mockdata['user_name'],
        email = user_mockdata['email'],
        xp = user_mockdata['xp'],
        cash = user_mockdata['cash'],
        password = user_mockdata['password']
    )

