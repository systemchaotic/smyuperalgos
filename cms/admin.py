from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Content, ContentAdmin)