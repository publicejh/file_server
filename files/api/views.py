from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from files.models import ImageInfo
from .serializers import ImageInfoSerializer
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser,
    FormParser
)


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
