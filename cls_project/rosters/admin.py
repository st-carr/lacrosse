from django.contrib import admin
from .models import Player, School, League, Division, Data_Flag

# Register your models here.






@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'state', 'school', 'height', 'weight',)
    list_editable = ('state',)

class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class LeagueAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(League, LeagueAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Division)
admin.site.register(Data_Flag)