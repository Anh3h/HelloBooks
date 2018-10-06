from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.ProfileList.as_view(), name='user-list'),
    path('users/<int:pk>', views.ProfileDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/fav-books', views.FavBooks.as_view(), name='fav-books'),
    path('users/<int:pk>/reading-list', views.ReadingList.as_view(), name='reading-list'),
]
