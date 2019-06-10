from rest_framework import serializers
from files.models import ImageInfo, ChatImageInfo


class ImageInfoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = ImageInfo
        fields = '__all__'


class ChatImageInfoSerializer(serializers.ModelSerializer):
    photo_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = ChatImageInfo
        fields = '__all__'
