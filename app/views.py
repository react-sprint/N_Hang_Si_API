from django.shortcuts import render
from .serializers import (NPoemRanksListSerializer, NPoemRegisterSerializer)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

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
    serializer_class = NPoemRegisterSerializer

    def create(self, request, *args, **kwargs):
        request.data['result_text'] = '!@'.join(request.data.pop('list_text'))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
