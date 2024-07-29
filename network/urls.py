from django.urls import path

from network.views import NetworkListCreateAPIView, NetworkUpdateDeleteAPIView

urlpatterns = [
    path(
        "networks/",
        NetworkListCreateAPIView.as_view(),
        name="networks_list_create"
    ),
    path(
        "networks/<int:pk>/",
        NetworkUpdateDeleteAPIView.as_view(),
        name="networks_update_delete"
    ),
]
