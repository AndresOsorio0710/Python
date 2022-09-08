from rest_framework.routers import DefaultRouter
from beauty_person_app.views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
urlpatterns = router.urls