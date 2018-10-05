from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.ProfileList.as_view(), name='user-list'),
    path('users/<int:pk>', views.ProfileDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/fav-books', views.FavBooks.as_view(), name='fav-books'),
    path('users/<int:pk>/reading-list', views.ReadingList.as_view(), name='reading-list'),
]
