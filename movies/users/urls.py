from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name="user-list"),
    path('users/create/', UserRegisterCreate.as_view(), name="user-create"),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user-detail"),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name="user-update"),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name="user-delete"),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  #login
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"), #refresh
]
