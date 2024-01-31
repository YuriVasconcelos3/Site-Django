# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('display_id', 'title', 'image', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
