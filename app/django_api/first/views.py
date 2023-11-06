from rest_framework.views import APIView
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from first.models import Board


class GetBoardList(APIView):

    api_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_STRING,
                                 description='유저 아이디'),
        },
        required=['id']
    )
    api_schema_response = {
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'idx': openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description='게시글 번호'
                    ),
                    'title': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='게시글 제목'
                    ),
                    'content': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='게시글 내용'
                    ),
                    'id': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='유저 아이디'
                    ),
                }
            ),
            description='게시글 리스트'
        ),
    }

    @swagger_auto_schema(tags=['게시판'],
                         operation_id='게시글 리스트',
                         request_body=api_schema,
                         responses=api_schema_response)
    def post(self, request):
        project_data = Board.objects.select_related().filter(
            id=request.data.get('id'))
        project_data_values = project_data.values(
            'idx', 'title', 'content', 'id', 'id__name', 'id__email')
        result_data = [{'id': i['id'],
                        'name': i['id__name'],
                        'email': i['id__email'],
                        'idx': i['idx'],
                        'title': i['title'],
                        'content': i['content']} for i in project_data_values]
        return HttpResponse(result_data)
