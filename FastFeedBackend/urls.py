from django.conf import settings
from django.conf.urls.static import static
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
                  path('orders/<int:order_id>/total/', order.OrderTotalPriceAPIView.as_view(), name='order-total'),
                  path('api/order/', order.OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='orders-api'),
                  path('api/owner/', owner.BusinessOwnerViewSet.as_view({'get': 'list', 'post': 'create'}), name='owner-api'),
                  path('api/orderitem/', order.OrderItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='orderitems-api'),
                  path('product/<int:product_id>/average-rating/', comment.ProductRatingAPIView.as_view(),
                       name='product-average-rating'),
                  path('orders/<int:order_id>/productsName/', order.OrderProductNameListAPIView.as_view(),
                       name='order-product_name-list'),
                  path('orders/<int:order_id>/productsID/', order.OrderProductIdListAPIView.as_view(),
                       name='order-product_id-list'),
                  path('product/<int:product_id>/rating/', comment.ProductRatingAPIView.as_view(),
                       name='product-rating'),
                  path('order-comments/', comment.OrderCommentViewSet.as_view({'get': 'list'}),
                       name='order-comment-list'),
                  path('stores/<int:store_id>/ratings/', comment.StoreRatingAPIView.as_view(), name='store-ratings'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
