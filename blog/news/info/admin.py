from django.contrib import admin
from .models import Pos

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)


admin.site.register(Pos, PostAdmin)

""" def Babe(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append("{} stays {}".format(key, value))
    return result
 
print(Babe(Asake='Ibadan', Arike='Lagos', Ayoka='Osun')) """