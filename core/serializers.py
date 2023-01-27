from rest_framework import serializers
from . import models


class UrlItemSerializer(serializers.ModelSerializer):
    """ Serializes a url item object """

    class Meta:
        model = models.UrlItem
        fields = ('id', 'user', 'address',
                  'threshold', 'created_on', 'updated_on',
                  'deleted_at', 'failed_times')

        read_only_fields = ('created_at', 'updated_at', 'user',
                            'id', 'failed_times', 'deleted_at')


class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestItem
        fields = ('id', 'created_at', 'updated_at', 'url', 'result')
