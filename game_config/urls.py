from rest_framework.routers import DefaultRouter
from .api.views import UserLevelViewSet, DifficultyViewSet

app_name = 'game_config'

router = DefaultRouter()

router.register('levels', UserLevelViewSet, basename='levels')
router.register('difficulties', DifficultyViewSet, basename='difficulties')

urlpatterns = router.urls
