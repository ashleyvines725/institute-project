from django.contrib import admin
from .models import BlogPost, BlogImage, BlogComment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'article_id')


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'comment_title', 'blog_comment',
                    'created_on')
    search_fields = ['blog_comment']


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogImage, PostImageAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
