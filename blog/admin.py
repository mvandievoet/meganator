from django.contrib import admin
from .models import BlogPost, BlogImage
from django.utils.html import format_html

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1  # Allows you to add one or more images when creating a blog post

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'event_date', 'head_image')  # Display head image and other details
    search_fields = ('title', 'section', 'content')
    list_filter = ('section', 'event_date')
    ordering = ('-event_date',)  # Order by newest posts first
    
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'section', 'event_date', 'head_image')
        }),
        ('Additional Images', {
            'fields': ('other_images',),  # For additional images
        }),
    )
    
    inlines = [BlogImageInline]  # Allows for adding multiple images in the admin

    def head_image_tag(self, obj):
        if obj.head_image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.head_image.url)
        return "-"
    head_image_tag.short_description = 'Head Image'

