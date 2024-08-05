from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # designs
    path('designes/', DesignerWorkViewSet.as_view({'get': 'list', 'post': 'create'}), name='designes'),
    path('designes/<int:id>/', DesignerWorkViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='designe'),
    # login/logout/signup/rreset-password
    path('register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('password-reset/', UserViewSet.as_view({'post': 'password_reset'}), name='password-reset'),
    path('password-reset-confirm/', UserViewSet.as_view({'post': 'password_reset_confirm'}),
         name='password-reset-confirm'),
    # Profile
    path('user-profile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-profile'),
    path('user-profile/<int:id>/', UserProfileViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-profile'),
    path('cocial-accounts/', UserSocialNetworkLinkViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='user-cocial-accounts'),
    path('cocial-accounts/<int:id>/', UserSocialNetworkLinkViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='user-cocial-accounts'),
    path('contacts/', UserContactDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='user--contacts'),
    path('contacts/<int:id>/', UserContactDataViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-contacts'),
    # Favorite
    path('favorites/', FavoriteViewSet.as_view({'get': 'list'}), name='favorites-list'),
    path('favorites/',
         FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='favorites-detail'),
    path('favorites/add_design/', FavoriteViewSet.as_view({'post': 'add_design'}), name='add-favorite'),
    path('favorites/remove_design/', FavoriteViewSet.as_view({'post': 'remove_design'}), name='remove-favorite-item'),
    # Like
    path('like/', LikeViewSet.as_view({'get': 'list'}), name='like-list'),
    path('like/',
         LikeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='like-detail'),
    path('like/add_design/', LikeViewSet.as_view({'post': 'add_design'}), name='add-like'),
    path('like/remove_design/', LikeViewSet.as_view({'post': 'remove_design'}), name='remove-like'),
    # Review
    path('reviews/', DesigneWorkRevewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review'),
    path('reviews/<int:id>', DesigneWorkRevewViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='review'),
    # Chat
    path('chat/', ChatViewSet.as_view({'get': 'list', 'post': 'create'}), name='chat'),
    path('chat/<int:id>/',
         ChatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='chat'),
    # Message
    path('messages/', ChatViewSet.as_view({'get': 'list', 'post': 'create'}), name='messages'),
    path('messages/<int:id>/',
         ChatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='messages'),
]
