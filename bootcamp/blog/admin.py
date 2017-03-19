from django.contrib import admin

# Register your models here.

from .models import Category,BlogPost  #importing the class of models.h

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'category', 'publish', 'created', 'updated']
	list_filter = ['author', 'updated', 'publish', 'category']
	list_editable = ['title']
	search_fields = ['title', 'content']
	list_per_page = 1

admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
