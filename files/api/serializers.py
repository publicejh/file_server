from rest_framework import serializers
from files.models import ImageInfo


class ImageInfoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        fields = ('user_id', 'sig_id', 'photo', 'photo_thumbnail', )
        model = ImageInfo
