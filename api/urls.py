from django.urls import path
from api import views as api_views

urlpatterns = [
    path("Points_of_interest/", api_views.POIListView.as_view()),
    path("Points_of_interest/<int:pk>/", api_views.POIDetailView.as_view()),
]
