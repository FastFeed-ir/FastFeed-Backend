from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from store import views as store
from subs import views as subscription
from owner import views as owner

router = DefaultRouter()
router.register('stores', store.StoreViewSet)
router.register('collections', store.CollectionViewSet)
router.register('products', store.ProductViewSet)
router.register('comments', store.CommentViewSet)
router.register('subscriptions', subscription.SubscriptionViewSet)
router.register('owners', owner.BusinessOwnerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
