from django.shortcuts import render
from .serializers import NPoemRanksListSerializer
from rest_framework import generics

from .models import NPoems


def serverstate(request):
    return render(request, 'index.html')


class NPoemRanksListAPI(generics.ListAPIView):
    serializer_class = NPoemRanksListSerializer

    default_limit = 20

    def get_queryset(self):
        query_params = self.request.query_params
        page = query_params['page'] if 'page' in query_params.keys() else 0

        queryset = NPoems.objects.order_by('like').all(
        )[page*self.default_limit:(page+1)*self.default_limit]

        return queryset
