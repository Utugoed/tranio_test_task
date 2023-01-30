from rest_framework import serializers
from shorter.models import ShortUrl


class CreateCodeSerializer(serializers.Serializer):
    url = serializers.URLField()


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ["pk", "url", "code", "usage_counter"]
