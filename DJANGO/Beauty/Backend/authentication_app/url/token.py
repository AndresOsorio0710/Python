from rest_framework.routers import DefaultRouter
from authentication_app.views import TokenViewSet

router = DefaultRouter()
router.register(r'token', TokenViewSet, basename='token')
urlpatterns = router.urls