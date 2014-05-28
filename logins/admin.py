from django.contrib import admin
from logins.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Adding game into the admin interface
class InfoInline(admin.StackedInline):
    model = Info.game.through
    extra = 1

# Adding department to admin interface
class InfoDInline(admin.StackedInline):
    model = Info.department.through
    extra = 1

# Customizing the fields
class InfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['title', 'url', 'name', 'password', 'comments']}),
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


