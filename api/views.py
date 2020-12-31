from core.models import PointOfInterest, TellYourStory, User
from api.serializers import POISerializer, TYSSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):	
        return User.objects.all()

class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'User_id'
    queryset = User.objects.all()       	


class POIListView(ListCreateAPIView):
    serializer_class = POISerializer

    def get_queryset(self):	
        # if the request method is GET, the queryset is all viewable POIs	
        # otherwise, the queryset is all POIs the current user owns	
        if self.request.method == "GET":	
            return PointOfInterest.objects.all()	

        return self.request.user.PointsOfInterest.all()

class POIDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = POISerializer
    lookup_url_kwarg = 'PointOfInterest_id'
    queryset = PointOfInterest.objects.all()

class TYSListView(ListCreateAPIView):
    serializer_class = TYSSerializer

    def get_queryset(self):
        # if the request method is GET, the queryset is all viewable TYSs
        # otherwise, the queryset is all TYSs the current user owns
        if self.request.method == "GET":
            return TellYourStory.objects.all()

        return self.request.user.TellYourStories.all() 

class TYSDetailView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = TYSSerializer
    lookup_url_kwarg = 'TellYourStory_id'
    queryset = TellYourStory.objects.all()  




    


# class POIListView(ListCreateAPIView):
#     serializer_class = POISerializer

#     def get_queryset(self):
#         return PointOfInterest.objects.for_user(self.request.user)

#     def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
