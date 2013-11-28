from django.contrib import admin
from logins.models import Department, Game

class GameInline(admin.StackedInline):
    model = Game
    extra = 1
    '''
    def game_namagame(object):
     return object.game.namegame
    '''


class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [GameInline]

    '''
    list_display = ['game_namegame',]
    '''
     
    list_filter = ['name']
    search_fields = ['name']

    '''
    def name_of_the_game(self):
        return self.game.name_of_the_game
    '''


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Game)

