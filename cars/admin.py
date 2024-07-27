from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    #用來顯示圖片縮略圖
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%;" />'.format(object.car_photo.url))
    

    # 設置欄位的 short_description
    thumbnail.short_description = 'car_photo'
     # 定義其他需要顯示的欄位
    list_display = ('car_title','thumbnail','color','model','year','body_style', 'fuel_type', 'is_featured')
    list_display_links = ('car_title', 'thumbnail',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style','fuel_type')
    list_filter = ('city','model','body_style','fuel_type')

# #用來顯示圖片縮略圖
#     def thumbnail(self, object):
#         return format_html('<img src="{}" width="40" style="border-radius: 50%;" />'.format(object.photo.url))
    

#     # 設置欄位的 short_description
#     thumbnail.short_description = 'avatar'

#     # 定義其他需要顯示的欄位
#     list_display = ('id','thumbnail','first_name','designation', 'create_date')
#     list_display_links = ('id','thumbnail', 'first_name')
#     search_fields = ('first_name', 'last_name', 'designation')
#     list_filter = ('designation',)