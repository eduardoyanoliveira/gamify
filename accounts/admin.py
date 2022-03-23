from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = CustomUser
    list_filter = ('email', 'user_name' , 'is_active')
    ordering = ('-created_at',)
    list_display = ('email', 'id', 'user_name',
                    'is_active', 'is_superuser', 'xp', 'cash', 'created_at')
    
    fieldsets = (
        (None, {'fields': ('email', 'user_name',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name',  'password1', 'password2', 'is_active', 'is_superuser', 'xp', 'cash', 'image')}
         ),
    )


admin.site.register(CustomUser, UserAdminConfig)