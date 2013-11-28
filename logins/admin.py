from django.contrib import admin
from logins.models import Department, Game

class GameInline(admin.StackedInline):
    model = Game
    extra = 1

class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [GameInline]


admin.site.register(Department, DepartmentAdmin)

