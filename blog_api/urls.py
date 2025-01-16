from django.urls import path
from .views import TaskListCreate, TaskDetail, CommentListCreate, CommentDetail
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]