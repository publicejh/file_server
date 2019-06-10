from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from files.models import ImageInfo, ChatImageInfo
from .serializers import ImageInfoSerializer, ChatImageInfoSerializer
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser,
    FormParser
)
import requests
import json
from django.conf import settings


class ImageInfoCreateView(APIView):
    queryset = ImageInfo.objects.all()
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ImageInfoSerializer

    def post(self, request):
        file = request.FILES['file']
        user_id = request.data['userId']
        sig_id = request.data['sigId']

        image_info_serializer = ImageInfoSerializer(data={'user_id': user_id, 'sig_id': sig_id, 'photo': file})

        if image_info_serializer.is_valid():
            image_info_serializer.save()

            return Response(image_info_serializer.data['photo_thumbnail'], status=status.HTTP_200_OK)
        else:
            return Response(image_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatImageUploadAndSendView(APIView):
    queryset = ChatImageInfo.objects.all()
    # parser_classes = (FileUploadParser,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ChatImageInfoSerializer

    def post(self, request):
        file = request.FILES['file']
        user_id = request.data['userId']
        chat_id = request.data['chatId']

        chat_image_info_serializer = ChatImageInfoSerializer(
            data={'user_id': user_id, 'chat_id': chat_id, 'photo': file}
        )

        if chat_image_info_serializer.is_valid():
            chat_image_info_serializer.save()

            data_json = json.dumps({
                'from': user_id,
                'is_file': True,
                'file_path': chat_image_info_serializer.data['photo_thumbnail'],
                'chat_id': chat_id
            })

            headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                       'Authorization': 'Api-Key ' + settings.CHAT_SERVER_API_KEY}
            res = requests.post(settings.CHAT_SERVER_UPLOAD_IMAGE_API_URL, data=data_json, headers=headers)

            print('xxxxx', res.content)

            if res.json().get('result') != 8200:
                return Response({'result': 400}, status=status.HTTP_200_OK)
                # return Response({'result': status_code['CHAT_MADE_FAIL']}, status=status.HTTP_200_OK)

            return Response(chat_image_info_serializer.data['photo_thumbnail'], status=status.HTTP_200_OK)
        else:
            return Response(chat_image_info_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
