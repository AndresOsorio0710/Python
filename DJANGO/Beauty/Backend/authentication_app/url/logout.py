from rest_framework.routers import DefaultRouter
from authentication_app.views import LogoutViewSet

router = DefaultRouter()
router.register(r'logout', LogoutViewSet, basename='logout')
urlpatterns = router.urls