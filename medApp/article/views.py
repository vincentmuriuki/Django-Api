# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import Article
from .models import Article
from serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()

        # the many params informs the serializer that it will be serializing more than a single article
        serializer = ArticleSerializer(articles, many=True)
        return response({"articles": serializer.data})