from django.contrib import admin
from django.utils.safestring import mark_safe


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'is_active', 'is_home', 'slug', 'selected_categories',)
    list_editable = ('is_active', 'is_home')
    list_filter = ('is_active', 'is_home', 'categories',)
    search_fields = ('title', 'image', 'description', 'is_active', 'is_home')
    readonly_fields = ('slug',)

    def selected_categories(self, obj):
        # return ", ".join([category.name for category in obj.categories.all()])
        html = "<ul>"
        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        html += "</ul>"
        return mark_safe(html)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    # list_editable = ('name',)
    list_filter = ('name', 'slug')
    search_fields = ('name',)
    readonly_fields = ('slug',)


from .models import Blog, Category

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
