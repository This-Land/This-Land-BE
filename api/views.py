from core.models import Point_of_interest
from api.serializers import POISerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class POIListView(ListCreateAPIView):
    serializer_class = POISerializer

    def get_queryset(self):
        # if the request method is GET, the queryset is all viewable POIs
        # otherwise, the queryset is all POIs the current user owns
        if self.request.method == "GET":
            return Point_of_interest.objects.all()

        return self.request.user.Points_of_interest.all()


# class POIListView(ListCreateAPIView):
#     serializer_class = POISerializer

#     def get_queryset(self):
#         return Point_of_interest.objects.for_user(self.request.user)

#     def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
