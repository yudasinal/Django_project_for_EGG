from django.contrib import admin
from logins.models import *

class InfoInline(admin.StackedInline):
    model = Info.game.through
    extra = 1

class InfoDInline(admin.StackedInline):
    model = Info.department.through
    extra = 1

class CustomUserAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'department', 'game')   #How to display ManyToMany? list_display does not handle it
admin.site.register(CustomUser, CustomUserAdmin)

'''
class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [InfoInline]
     
    list_filter = ['name']
    search_fields = ['name']
'''

class InfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['organization_name', 'user_name', 'password']}),
    ]
    inlines = [InfoInline, InfoDInline]

admin.site.register(Department)
admin.site.register(Game)
admin.site.register(Info, InfoAdmin)

