from rest_framework import serializers
from models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerFiels()

    def create(self, validate_data):
        return Article.objects.create(**validate_data)