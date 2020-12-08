from django.contrib import admin
from .models import NPoems


class NPoemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'level', 'created_at']
    list_filter = ['word', 'level']
    list_per_page = 10
    search_fields = ['nickname']


admin.site.register(NPoems, NPoemsAdmin)
