from django.contrib import admin

from lists.models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'user', 'privacy')
    list_filter = ('type', 'user', 'privacy')
    search_fields = ('name', 'description')

admin.site.register(List, ListAdmin)
