from core.models import PointOfInterest, TellYourStory
from api.serializers import POISerializer, TYSSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class POIListView(ListCreateAPIView):
    serializer_class = POISerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):	
        # if the request method is GET, the queryset is all viewable POIs	
        # otherwise, the queryset is all POIs the current user owns	
        if self.request.method == "GET":	
            return PointOfInterest.objects.all()	
        return self.request.user.PointsOfInterest.all()

class POIDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = POISerializer
    # permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'PointOfInterest_id'
    queryset = PointOfInterest.objects.all()
    

class TYSListView(ListCreateAPIView):
    serializer_class = TYSSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # if the request method is GET, the queryset is all viewable TYSs
        # otherwise, the queryset is all TYSs the current user owns
        if self.request.method == "GET":
            return TellYourStory.objects.all()

        return self.request.user.TellYourStories.all() 

class TYSDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TYSSerializer
    # permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'TellYourStory_id'
    queryset = TellYourStory.objects.all()  
