from rest_framework.views import APIView
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.parsers import MultiPartParser
import redis
import pika
import cv2
import uuid
import numpy as np
import json
import os
from django.conf import settings

rds = redis.StrictRedis(host=settings.REDIS_HOST, db=0)

input_video_path = settings.INPUT_VIDEO_PATH
output_video_path = settings.OUTPUT_VIDEO_PATH

connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.MQ_HOST,heartbeat=0))
channel = connection.channel()

queue_name = settings.PRIVATE_QUEUE_NAME
channel.queue_declare(queue=queue_name)

class FileView(APIView):
    parser_classes = [MultiPartParser]
    api_schema = [
        openapi.Parameter('file', in_=openapi.IN_FORM, type=openapi.TYPE_FILE, description='파일'),
        openapi.Parameter('option', in_=openapi.IN_FORM, type=openapi.TYPE_STRING, description='옵션'),
    ]
    api_schema_response = {
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_FILE
        ),
    }
    @swagger_auto_schema(tags=['파일'],
                         operation_id='파일 업로드',
                         manual_parameters=api_schema,
                         responses=api_schema_response)
    def post(self, request):
        file = request.FILES.get('file')
        file_data = file.read()
        file_name = file.name
        option = request.POST.get('option')
        if option == 'save':
            with open('/app/' + file_name, 'wb') as f:
                f.write(file_data)
        return HttpResponse(content=file_data)