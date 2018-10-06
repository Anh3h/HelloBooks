from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.TopicList.as_view(), name="topic-list"),
    path('topics/<int:pk>', views.TopicDetail.as_view(), name="topic-detail"),
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>', views.BookDetails.as_view(), name="book-detail"),
]
