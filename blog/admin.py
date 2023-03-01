from django.contrib import admin

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'is_active', 'is_home','slug')
    list_editable = ('is_active', 'is_home')
    list_filter = ('title', 'image', 'description', 'is_active', 'is_home')
    search_fields = ('title', 'image', 'description', 'is_active', 'is_home')
    readonly_fields = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    # list_editable = ('name',)
    list_filter = ('name','slug')
    search_fields = ('name',)
    readonly_fields = ('slug',)

from .models import Blog, Category

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
