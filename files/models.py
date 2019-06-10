from django.db import models
import os
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


def set_filename_format(now, instance, filename):
    """ file format setting e.g) {user_id}-{microsecond}{extension} 1301-158859.png """
    return '{user_id}-{microsecond}{extension}'.format(user_id=instance.user_id, microsecond=now.microsecond,
                                                       extension=os.path.splitext(filename)[1], )


def user_directory_path(instance, filename):
    """ image upload directory setting e.g)
    images/{year}/{month}/{day}/{filename} images/2016/7/12/1301-158859.png """
    now = datetime.now()
    path = 'images/{year}/{month}/{day}/{filename}'.format(year=now.year, month=now.month, day=now.day,
                                                           filename=set_filename_format(now, instance, filename), )
    return path


class ImageInfo(models.Model):
    user_id = models.IntegerField()
    sig_id = models.IntegerField()
    photo = models.ImageField(upload_to=user_directory_path)
    photo_thumbnail = ImageSpecField(
        source='photo', 		   # 원본 ImageField 명
        processors=[Thumbnail(400, 400)],   # 처리할 작업목록
        format='JPEG',		   # 최종 저장 포맷
        options={'quality': 60}  # 저장 옵션(JPEG 압축률 설정)
    )

    def __str__(self):
        return self.user_id


class ChatImageInfo(models.Model):
    user_id = models.IntegerField()
    chat_id = models.IntegerField()
    photo = models.ImageField(upload_to=user_directory_path)
    photo_thumbnail = ImageSpecField(
        source='photo', 		   # 원본 ImageField 명
        processors=[Thumbnail(100, 100)],   # 처리할 작업목록
        format='JPEG',		   # 최종 저장 포맷
        options={'quality': 60}  # 저장 옵션(JPEG 압축률 설정)
    )
