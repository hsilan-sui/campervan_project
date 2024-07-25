from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    #用來顯示圖片縮略圖
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%;" />'.format(object.photo.url))
    

    # 設置欄位的 short_description
    thumbnail.short_description = 'avatar'

    # 定義其他需要顯示的欄位
    list_display = ('id','thumbnail','first_name','designation', 'create_date')
    list_display_links = ('id','thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


# Register your models here.
#admin.site.register(Team) # 管理model註冊到admin後台管理介面的函式
#通過這個函數，可以告訴 Django 管理員界面需要管理哪些模型（即資料表）以及如何展示它們
