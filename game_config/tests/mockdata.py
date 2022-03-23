from ..models import UserLevel
from ..models import Difficulty

user_level_mockdata1 = {
    "name": "UserLevel",
    "pts": 30
}

def create_user_level_mock(user_level_mockdata) -> UserLevel:
    return UserLevel.objects.create(name =user_level_mockdata['name'], pts= user_level_mockdata['pts'])
    

difficulty_mockdata1 = {
    "name": 'Difficulty',
    "color": '#000',
    "pts": 100   
}   

def create_difficulty_mock(difficulty_mockdata) -> Difficulty:
    return Difficulty.objects.create(
        name = difficulty_mockdata['name'],
        color = difficulty_mockdata['color'],
        pts = difficulty_mockdata['pts']
    ) 
   
       
    