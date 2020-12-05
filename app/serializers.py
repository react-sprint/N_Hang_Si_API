from .models import NPoems
from rest_framework import serializers, fields


class NPoemRanksListSerializer(serializers.ModelSerializer):
    page = fields.IntegerField(min_value=0, required=False)

    class Meta:
        model = NPoems
        fields = ('id', 'nickname', 'level', 'word',
                  'result_text', 'time', 'time_out', 'like', 'page',)

    def to_representation(self, instance):
        return instance.get_rank_info()


class NPoemRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = NPoems
        fields = ('nickname', 'level', 'word',
                  'result_text', 'time', 'time_out')
