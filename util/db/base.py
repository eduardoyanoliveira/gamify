from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
        ordering = ['-created_at']

class BaseNameField(Base):
    name = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True
       
        
