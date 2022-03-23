from rest_framework.routers import DefaultRouter
from .api.views import UserViewSet

app_name = 'accounts'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls
