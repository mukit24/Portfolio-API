from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

@api_view(['GET'])
def getAllProjects(request):
    projects = Project.objects.all().order_by('-priority')
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getTopProjects(request):
    projects = Project.objects.all().order_by('-priority')[0:6]
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def projectDetails(request,id):
    try:
        project = Project.objects.get(id=id)
        serializer = ProjectSerializer(project, many=False)
        print(serializer.data)
        return Response(serializer.data)
    except:
        return Response({'error': 'Project Not Found'},status=status.HTTP_400_BAD_REQUEST)
