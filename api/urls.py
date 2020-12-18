from django.urls import path
from api import views as api_views

urlpatterns = [
    path("pointsofinterest/", api_views.POIListView.as_view()),
    # path("pointsofinterest/<int:pk>/", api_views.POIDetailView.as_view()),
    path("tellyourstory/", api_views.TYSListView.as_view()),
]
