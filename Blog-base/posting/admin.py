from django.contrib import admin
from .models import Posting

# Register your models here.

class PostingAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'create_at')
    search_fields = ('judul', 'konten', 'penulis__username')
    list_filter = ('create_at', 'penulis')
    list_per_page = 3
    ordering = ('-create_at',)

admin.site.register(Posting, PostingAdmin)
