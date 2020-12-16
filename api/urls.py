from django.urls import path
from api import views as api_views

urlpatterns = [
    # path("points-of-interest/", api_views.POIListView.as_view()),
    path("points-of-interest/", api_views.POIListView.as_view()),
]
