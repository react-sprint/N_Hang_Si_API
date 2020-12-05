from .models import NPoems
from rest_framework import serializers, fields


class NPoemRanksListSerializer(serializers.ModelSerializer):
    page = fields.IntegerField(min_value=0, required=False)

    class Meta:
        model = NPoems
        fields = ('id', 'nickname', 'level', 'word',
                  'result_text', 'time', 'time_out', 'like', 'page',)
