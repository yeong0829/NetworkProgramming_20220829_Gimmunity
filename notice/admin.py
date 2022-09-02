from django.contrib import admin

# Register your models here.
from notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title','content','create_at','modify_at')
    list_filter = ('modify_at',)
    search_fields = ('title','content')