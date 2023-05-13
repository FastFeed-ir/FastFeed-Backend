from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from azbankgateways.urls import az_bank_gateways_urls

from comment import views as comment
from menu import views as menu
from order import views as order
from owner import views as owner
from store import views as store
from subs import views as subscription
from payments.views import go_to_gateway_view, callback_gateway_view

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
                  path('bankgateways/', az_bank_gateways_urls()),
                  path('go-to-gateway/', go_to_gateway_view),
                  path('callback-gateway/', callback_gateway_view),
              ] + router.urls
