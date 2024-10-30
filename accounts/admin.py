from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


# class UserProfileAdmin(admin.ModelAdmin):
#     def thumbnail(self, object):
#         return format_html('<img src="()" width="30" style= "border-radius:50%;">'.format(object.profile_picture.url))
    
#     thumbnail.short_description = 'Profile Picture'
#     list_display = ('user', 'city','country' )

admin.site.register(Account, AccountAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)