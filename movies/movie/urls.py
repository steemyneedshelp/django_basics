from django.urls import path # type: ignore
from .views import MovieListView , MovieListCreate, MovieListRetrieve, MovieListDelete, MovieListUpdate
from rest_framework.permissions import IsAuthenticated # type: ignore

urlpatterns = [
    path('movielistview/', MovieListView.as_view(), name="movielistview"),
    path('movielistview/create/', MovieListCreate.as_view(), name="movielistcreate"),
    path('movielistview/<int:pk>/', MovieListRetrieve.as_view(), name="movielistretrieve"),
    path('movielistview/<int:pk>/update/', MovieListUpdate.as_view(), name="movielistupdate"),
    path('movielistview/<int:pk>/delete/', MovieListDelete.as_view(), name="movielistdelete")
]
