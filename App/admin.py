# from django.contrib import admin
#
# # Register your models here.
# from .models import Post
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status', 'created_on','image')
#     list_filter = ('status',)
#     search_fields = ['title', 'content']
#
#
# admin.site.register(Post, PostAdmin)
from django.contrib import admin

from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass