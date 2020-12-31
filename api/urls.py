from django.urls import path
from api import views as api_views

urlpatterns = [
    path("userpass/", api_views.UserListView.as_view()),
    path("pointsofinterest/", api_views.POIListView.as_view()),
    path('pointsofinterest/<int:PointOfInterest_id>/', api_views.POIDetailView.as_view()),
    path("tellyourstory/", api_views.TYSListView.as_view()),
    path('tellyourstory/<int:TellYourStory_id>/', api_views.TYSDetailView.as_view()),
]
