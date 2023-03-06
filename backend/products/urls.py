from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = 'product'

router = DefaultRouter()
router.register(r'products', viewsets.ProductViewSet, basename='product-view-set')
router.register(r'images', viewsets.PictureViewSet, basename='image-view-set')

urlpatterns = [
    *router.urls
]
