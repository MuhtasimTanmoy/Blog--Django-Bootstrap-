from django.contrib import admin

# Register your models here.

from .models import Post

class postModel(admin.ModelAdmin):
    list_display=["title","timestamp"]
    list_filter=["timestamp"]
    search_fields=["title","content"]
    class Meta:
        model=Post

admin.site.register(Post,postModel)
