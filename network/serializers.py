from rest_framework import serializers

from network.models import Network


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.__class__(value, context=self.context)
        return serializer.data


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = [
            'name',
            'network',
            'liability',
            'created_at',
        ]


class NetworkListSerializer(NetworkSerializer):
    network = RecursiveSerializer(read_only=True, required=False)


class NetworkCreateSerializer(NetworkSerializer):
    pass


class NetworkListCreateSerializer(NetworkSerializer):
    def get_serializer_class(self):
        if self.context['request'].method in ['GET']:
            return NetworkListSerializer
        return NetworkCreateSerializer

    def to_representation(self, instance):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instance, context=self.context)
        return serializer.data


class NetworkUpdateSerializer(NetworkListSerializer):
    liability = serializers.FloatField(read_only=True)
