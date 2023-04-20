from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from news_app.models import Comment
from news_app.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def create(self, request):

    #     serializer = self.get_serializer(data={})

