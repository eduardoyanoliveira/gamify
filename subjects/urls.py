from rest_framework.routers import DefaultRouter
from .api.views import SubjectViewSet, ContentViewSet, KeywordViewSet

app_name = 'subjects'

router = DefaultRouter()

router.register('subjects', SubjectViewSet, basename='subjects')
router.register('contents', ContentViewSet, basename='contents')
router.register('keywords', KeywordViewSet, basename='keywords')


urlpatterns = router.urls
