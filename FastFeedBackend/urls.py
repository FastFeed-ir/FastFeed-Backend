from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from comment import views as comment
from menu import views as menu
from order import views as order
from owner import views as owner
from store import views as store
from subs import views as subscription

router = DefaultRouter()
router.register('stores', store.StoreViewSet)
router.register('collections', menu.CollectionViewSet)
router.register('products', menu.ProductViewSet)
router.register('comments', comment.CommentViewSet)
router.register('subscriptions', subscription.SubscriptionViewSet)
router.register('owners', owner.BusinessOwnerViewSet)
router.register('orders', order.OrderViewSet)
router.register('order_items', order.OrderItemViewSet)
router.register('ratings', comment.RatingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('stores/<int:store_id>/tables/<int:table_number>/last-order/', order.LastOrderView.as_view()),
    path('orders/<int:order_id>/productsID/', order.OrderProductIdListAPIView.as_view(), name='order-product_id-list'),
    path('orders/<int:order_id>/productsName/', order.OrderProductNameListAPIView.as_view(),
         name='order-product_name-list'),
    path('order-comments/', comment.OrderCommentViewSet.as_view({'get': 'list'}), name='order-comment-list'),
] + router.urls
