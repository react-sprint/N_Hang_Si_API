from django.shortcuts import render
from .serializers import (NPoemRanksListSerializer,
                          NPoemRegisterSerializer,
                          NPoemLikeSerializer)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import exceptions

from .models import NPoems


def serverstate(request):
    return render(request, 'index.html')


class NPoemRanksListAPI(generics.ListAPIView):
    serializer_class = NPoemRanksListSerializer

    default_limit = 10

    def get_queryset(self):
        query_params = self.request.query_params
        page = int(query_params['page']
                   if 'page' in query_params.keys() else 0)
        queryset = NPoems.objects.order_by('-like', '-id').all(
        )[page*self.default_limit:(page+1)*self.default_limit]

        return queryset


class NPoemRegisterAPI(generics.CreateAPIView):
    def post(self, request):
        try:
            if(len(request.data['word']) != len(request.data['list_text'])):
                raise exceptions.ValidationError("error")
            request.data['result_text'] = '!@'.join(
                request.data.pop('list_text'))
            serializer = NPoemRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            raise exceptions.ValidationError("error")


class NPoemIncreaseLikeAPI(generics.UpdateAPIView):
    serializer_class = NPoemLikeSerializer
    queryset = NPoems.objects.all()

    def get_object(self):
        object = super().get_object()
        object.like = object.like + 1
        return object


class NPoemDecreaseLikeAPI(generics.UpdateAPIView):
    serializer_class = NPoemLikeSerializer
    queryset = NPoems.objects.all()

    def get_object(self):
        object = super().get_object()
        object.like = object.like - 1 if object.like > 0 else 0
        return object
