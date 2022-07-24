from curses.ascii import US
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, FriendRequest

# Register your models here.
class UserAdminConfig(UserAdmin):
        readonly_fields = ["date_joined"]
        ordering = ('date_joined',)
        list_display = ('email', 'username', 'is_staff', 'is_active', 'date_joined')
        search_fields = ('email', 'username',)

        add_fieldsets = UserAdmin.add_fieldsets + (
                (None, {'fields': ('email',)}),
        )
        fieldsets = (
                (None, {
                "fields": (
                        ('email', 'username', 'password', 'bio', 'profile_img', 'hide_email', 'is_staff', 'is_active')
                        
                ),
                }),
        )
        
        model = Account

admin.site.register(Account, UserAdminConfig)
admin.site.register(FriendRequest)