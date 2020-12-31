from core.models import PointOfInterest, TellYourStory
from api.serializers import POISerializer, TYSSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class POIListView(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = POISerializer

    def get_queryset(self):	
        # if the request method is GET, the queryset is all viewable POIs	
        # otherwise, the queryset is all POIs the current user owns	
        if self.request.method == "GET":	
            return PointOfInterest.objects.all()	

        return self.request.user.PointsOfInterest.all()



class POIDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = POISerializer
    lookup_url_kwarg = 'PointOfInterest_id'
    queryset = PointOfInterest.objects.all()

class TYSListView(ListCreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TYSSerializer

    def get_queryset(self):
        # if the request method is GET, the queryset is all viewable TYSs
        # otherwise, the queryset is all TYSs the current user owns
        if self.request.method == "GET":
            return TellYourStory.objects.all()

        return self.request.user.TellYourStories.all() 

class TYSDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = TYSSerializer
    lookup_url_kwarg = 'TellYourStory_id'
    queryset = TellYourStory.objects.all()  


class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token = Token.objects.get_or_create(user=request.user)[0]

        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'token': str(token.key),  # None 
        }
        return Response(content)


    


# class POIListView(ListCreateAPIView):
#     serializer_class = POISerializer

#     def get_queryset(self):
#         return PointOfInterest.objects.for_user(self.request.user)

#     def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
