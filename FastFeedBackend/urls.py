from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from store import views as store
from product import views as product
from comment import views as comment
from collection import views as collection
from subs import views as subscription
from order import views as order
from owner import views as owner
from rating import views as rating

router = DefaultRouter()
router.register('stores', store.StoreViewSet)
router.register('collections', collection.CollectionViewSet)
router.register('products', product.ProductViewSet)
router.register('comments', comment.CommentViewSet)
router.register('subscriptions', subscription.SubscriptionViewSet)
router.register('owners', owner.BusinessOwnerViewSet)
router.register('orders', order.OrderViewSet)
router.register('order_items', order.OrderItemViewSet)
router.register('ratings', rating.RatingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
