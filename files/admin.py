from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import ImageInfo


class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='photo_thumbnail')


admin.site.register(ImageInfo, ImageInfoAdmin)
