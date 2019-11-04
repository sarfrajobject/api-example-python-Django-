from django.contrib import admin
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','Email','Password')
admin.site.register(Register,RegisterAdmin)