from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index, name='home'),
    path('', views.loginUser, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    
    path('libview/', views.libview, name='libview'),
    path('bookview/<int:id>', views.bookview, name='bookview'),
    path('profileview/<int:id>', views.profileview, name='profileview'),
    path('managebooks/', views.managebooks, name='managebooks'),
    path('addbook/', views.addbook, name='addbook'),
    path('editbook/<str:pk>', views.editbook, name='editbook'),
    path('deletebook/<str:pk>', views.deletebook, name='deletebook'),
    path('issuebook/<str:bookname>/<str:stid>', views.issuebook, name='issuebook'),
    path('viewrequests/', views.viewrequests, name='viewrequests'),
    path('deleterequest/<int:request_id>', views.deleterequest, name='deleterequest')
]