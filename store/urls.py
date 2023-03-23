from rest_framework.routers import DefaultRouter
from store import views

router = DefaultRouter()
router.register('stores', views.StoreViewSet)
router.register('collections', views.CollectionViewSet)
router.register('products', views.ProductViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = router.urls
