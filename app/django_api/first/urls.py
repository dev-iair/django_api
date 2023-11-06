from django.urls import path
from first.views import GetBoardList

urlpatterns = [
  path('list', GetBoardList.as_view()),
]