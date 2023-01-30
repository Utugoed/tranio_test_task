from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.parsers import JSONParser

from api.serializers import CreateCodeSerializer, ShortUrlSerializer
from shorter.models import ShortUrl

# Create your views here.
@api_view(['GET', 'POST'])
def short_urls(request):
    if request.method == "GET":
        urls = ShortUrl.objects.all()
        serializer = ShortUrlSerializer(urls, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CreateCodeSerializer(data=data)
        if serializer.is_valid():
            new_url = ShortUrl.create_code(url=data["url"])
            return JsonResponse(new_url.to_dict(), status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)


