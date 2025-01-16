from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task, Comment
from .serializers import TaskListSerializer, TaskDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        due_date = self.request.query_params.get('due_date')

        if status:
            queryset = queryset.filter(status=status)
        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.request.query_params.get('task')
        if task_id:
            return self.queryset.filter(task_id=task_id)
        return self.queryset

    def perform_create(self, serializer):
        task_id = self.request.data.get('task')
        task = Task.objects.get(id=task_id)
        serializer.save(author=self.request.user, task=task)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)









#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def api_tasks(request):
#     if request.method == 'GET':
#         tasks = Task.objects.filter(user=request.user)
#         serializer = TaskListSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def api_task_detail(request, pk):
#     task = get_object_or_404(Task, pk=pk, user=request.user)
#
#     if request.method == 'GET':
#         serializer = TaskDetailSerializer(task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskDetailSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def api_comments(request, task_pk):
#     task = get_object_or_404(Task, pk=task_pk, user=request.user)
#
#     if request.method == 'GET':
#         comments = Comment.objects.filter(task=task)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user, task=task)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def api_comment_detail(request, task_pk, pk):
#     task = get_object_or_404(Task, pk=task_pk, user=request.user)
#     comment = get_object_or_404(Comment, pk=pk, task=task)
#
#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response({'message': 'Комментарий успешно удален'}, status=status.HTTP_204_NO_CONTENT)
#