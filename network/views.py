from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from network.models import Network
from network.serializers import NetworkListCreateSerializer, NetworkUpdateSerializer


class NetworkListCreateAPIView(ListCreateAPIView):
    serializer_class = NetworkListCreateSerializer

    def get_queryset(self):
        if country := self.request.query_params.get("country"):
            return Network.objects.filter(contacts__city__country__name__icontains=country)
        return Network.objects.all()


class NetworkUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkUpdateSerializer
