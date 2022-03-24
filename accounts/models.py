from django.db import models
from util.db import base

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, user_name, password, **other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        
        if len(password) < 6:
            raise ValueError('Password needs to have at least 6 characters')


        return self.create_user(email, user_name, password, **other_fields)
    

    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                         **other_fields)
        
        if len(password) < 6:
            raise ValueError('Password needs to have at least 6 characters')
        else:
            user.set_password(password)
            
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin, base.Base):
    
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='media/images/user', blank=True, null=True)
    xp = models.IntegerField(default=0)
    cash = models.IntegerField(default=0)
    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']
    
    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.user_name
    
    
    def save(self, *args, **kwargs) -> None:
        if self.xp < 0:
            raise ValueError('Xp can not be negative')
        
        if self.cash < 0:
            raise ValueError('Cash can not be negative')
        
        if len(self.password) < 6:
            raise ValueError('Password needs to have at least 6 characters')
        
        return super().save(*args, **kwargs)
    
    
    class Meta:
        db_table = 'tbl_user'
    
