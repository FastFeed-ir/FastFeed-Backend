from django.urls import path
from .views import BusinessOwnerList, BusinessOwnerDetail

urlpatterns = [
    path('cro/', BusinessOwnerList.as_view()),
    path('cro/<int:pk>/', BusinessOwnerDetail.as_view()),
]
