from django.test import TestCase
from .test_mockdata import difficulty_mockdata1, user_level_mockdata1, create_difficulty_mock, create_user_level_mock
from ..models import UserLevel, Difficulty

# UserLevel Tests
class TestUserLevelCase(TestCase):
    
    def setUp(self) -> None:
        create_user_level_mock(user_level_mockdata1)
    

    def test_str(self) -> None:
        user_level = UserLevel.objects.get(id=1)
        self.assertEqual(str(user_level), user_level_mockdata1['name'])  
        
        
    def test_create(self) -> None:
        user_level = UserLevel.objects.get(id=1)
        name = user_level.name
        pts = user_level.pts
        self.assertEqual(name, user_level_mockdata1['name'])
        self.assertEqual(pts, user_level_mockdata1['pts'])
    
    
    def test_pts_error(self) -> None:
        user_level = UserLevel.objects.get(id=1)
        user_level.pts = -10
        
        with self.assertRaises(ValueError):
            user_level.save()
          


# Difficulty Tests
class TestDifficultyCase(TestCase):
    
    def setUp(self) -> None:
        create_difficulty_mock(difficulty_mockdata1)
      
    
    def test_create(self) -> None:
        difficulty = Difficulty.objects.get(id=1)
        name = difficulty.name
        color = difficulty.color
        pts = difficulty.pts
        
        self.assertEqual(name, difficulty_mockdata1['name'])
        self.assertEqual(pts, difficulty_mockdata1['pts'])
        self.assertEqual(color, difficulty_mockdata1['color'])
  
    
    def test_str(self) -> None:
        difficulty = Difficulty.objects.get(id=1)
        self.assertEqual(str(difficulty), difficulty_mockdata1['name']) 
    
    
    def test_pts_error(self) -> None:
        difficulty = Difficulty.objects.get(id=1)
        difficulty.pts = -10
        
        with self.assertRaises(ValueError):
            difficulty.save()   


    def test_color_error(self) -> None:
        difficulty = Difficulty.objects.get(id=1)
        difficulty.color = 'test'
        
        with self.assertRaises(ValueError):
            difficulty.save()   