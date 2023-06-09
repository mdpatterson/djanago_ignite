from rest_framework import serializers
from snippets.models import Snippet
from django.db import models


class SnippetSerializer(serializers.Serializer):
    #created = models.DateTimeField(auto_now_add=True)
    #title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        #instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        return instance