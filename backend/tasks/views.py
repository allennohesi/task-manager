from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):
    """
    ViewSet for viewing and editing Task instances.
    """
    
    def list(self, request):
        """
        List all tasks
        """
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        Create a new task
        """
        title = request.data.get('title')
        description = request.data.get('description', '')
        completed = request.data.get('completed', False)
        
        if not title:
            return Response({'detail': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed
        )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a specific task by ID
        """
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk=None):
        """
        Update a task (full update - title & description)
        """
        try:
            task = Task.objects.get(pk=pk)
            title = request.data.get('title')
            description = request.data.get('description', '')
            
            if not title:
                return Response({'detail': 'Title is required.'}, status=status.HTTP_400_BAD_REQUEST)
            
            task.title = title
            task.description = description
            task.save()
            
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    def partial_update(self, request, pk=None):
        """
        Toggle task completed status only (PATCH)
        """
        try:
            task = Task.objects.get(pk=pk)
            # Toggle completed status
            task.completed = not task.completed
            task.save()
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, pk=None):
        """
        Delete a task (hard delete)
        """
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

