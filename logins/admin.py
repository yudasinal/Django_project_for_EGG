from django.contrib import admin
from logins.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class InfoInline(admin.StackedInline):
    model = Info.game.through
    extra = 1

class InfoDInline(admin.StackedInline):
    model = Info.department.through
    extra = 1

class InfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['organization_name', 'url', 'user_name', 'password', 'comments']}),
    ]
    inlines = [InfoInline, InfoDInline]

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'custom_user'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (CustomUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)    
admin.site.register(Department)
admin.site.register(Game)
admin.site.register(Info, InfoAdmin)

'''
class CustomUserAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'department', 'game')   #How to display ManyToMany? list_display does not handle it
admin.site.register(CustomUser, CustomUserAdmin)

'''

'''
class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [InfoInline]
     
    list_filter = ['name']
    search_fields = ['name']
'''

