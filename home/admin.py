from django.contrib import admin
from home.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'body')
    search_fields = ('slug',)
    list_filter = ('updated',)
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('user',)


admin.site.register(Post, PostAdmin)
