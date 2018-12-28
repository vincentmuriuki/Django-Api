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

    def post(self, request):
        article = request.data.get('article')

        # create an article from the above data
        serializer = ArticleSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()

        return Response({"success": "Article '{}' created successfully".format(article_saved.title)})


    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
