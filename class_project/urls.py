from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='redirect_to_about'),
    path('redirect/', views.redirect),
    path('about/', views.about, name='about'),
    path('book-list/', views.book_list, name='book-list'),
    path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),
]