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

super_mockdata = {
    "user_name": 'super2',
    "email" : 'test@super',
    "password": 'SW@master35',
    "is_superuser": True,
    "is_active": True
}
        

def create_user_mock(user_mockdata) -> CustomUser:
    return CustomUser.objects.create(
        user_name= user_mockdata['user_name'],
        email = user_mockdata['email'],
        xp = user_mockdata['xp'],
        cash = user_mockdata['cash'],
        password = user_mockdata['password']
    )


def create_super_mock(super_mockdata) -> CustomUser:
    return CustomUser.objects.create_user(
        user_name = super_mockdata['user_name'],
        email= super_mockdata['email'],
        password = super_mockdata['password'],
        is_superuser= super_mockdata['is_superuser'],
        is_active = super_mockdata['is_active']
    )
