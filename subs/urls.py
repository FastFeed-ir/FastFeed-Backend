from django.urls import path
from .views import StoreList, StoreDetail, SubscriptionList, SubscriptionDetail

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetail.as_view(), name='store-detail'),
    path('subs/', SubscriptionList.as_view(), name='subscription-list'),
    path('subs/<int:pk>/', SubscriptionDetail.as_view(), name='subscription-detail'),
]
