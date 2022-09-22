from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('redirect/', views.redirect),
    # path('about/', views.about, name='about'),
    # path('book-list/', views.book_list, name='book-list'),
    # path('book-detail/<int:pk>/', views.book_details, name='book-detail'),
    # path('books/', views.book_list, name='book-list'),
    path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetails.as_view(), name='book-details'),
    path('publishers/', views.PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', views.PublisherDetails.as_view(), name='publisher-details'),
]
