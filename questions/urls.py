from rest_framework.routers import DefaultRouter
from .api.views import QuestionViewSet, AnswerViewSet

app_name ='questions'

router = DefaultRouter()

router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet, basename='answers')

urlpatterns = router.urls