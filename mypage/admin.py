# admin.py
from django.contrib import admin
from .models import Comment, Store

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')  # 管理画面で表示するフィールド
    search_fields = ('user__username', 'content')  # 検索ボックスで検索できるフィールド
    list_filter = ('created_at',)  # フィルタリングオプション

admin.site.register(Comment, CommentAdmin)

admin.site.register(Store)
