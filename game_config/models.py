from django.db import models
from util.db import base
from util.colors.funcs import is_color

# Create your models here.
class UserLevel(base.BaseNameField):
    pts = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    
    def save(self, *args, **kwargs) -> None:
        if self.pts < 0:
            raise ValueError('Pts can not be negative')
        
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'tbl_level'


class Difficulty(base.BaseNameField):
    color = models.CharField(max_length=50)
    pts = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    
    def save(self, *args, **kwargs) -> None:
        
        if self.pts < 0:
            raise ValueError('Pts can not be negative')
        
        if not is_color(self.color):
            raise ValueError('This is not a valid color')
        
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'tbl_difficulty'