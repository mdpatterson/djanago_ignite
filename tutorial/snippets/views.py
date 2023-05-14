from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
#from .helpers.sql_helper import TableNames, Query, TestData
#from pyignite import Client
from .my_ignite.my_ignite import cleanuptables, my_data_from_ignite
import io
from rest_framework.renderers import JSONRenderer

@csrf_exempt
#def snippet_list(request):
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        cleanuptables()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':  #and a change here
         my_data = []
         try:
             data = JSONParser().parse(request)
             if data['code'] == 'option1':
                 my_data = my_data_from_ignite('1')
                 cleanuptables()
             elif data['code'] == 'option2':
                 my_data = my_data_from_ignite('10')
                 cleanuptables()
             else:
                 pass
         except:
             cleanuptables()

         my_dict = {'code': str(my_data)}
         serializer = SnippetSerializer(data=my_dict)
         if serializer.is_valid():
             if not my_data:
                 my_list=['Option not valid']
                 my_dict = {'code': str(my_list)}
                 serializer = SnippetSerializer(data=my_dict)
                 if serializer.is_valid():
                     return JsonResponse(serializer.data, status=201)
                 else:
                     return JsonResponse(serializer.errors, status=400)
             else:
                return JsonResponse(serializer.data, status=201)
         return JsonResponse(serializer.errors, status=400)

