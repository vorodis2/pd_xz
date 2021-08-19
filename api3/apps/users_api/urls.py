from rest_framework.routers import DefaultRouter
from djoser.views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = router.urls
