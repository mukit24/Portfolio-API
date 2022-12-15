from django.urls import path
from .views import getAllProjects, projectDetails

app_name = 'projects'
urlpatterns = [
    path('',getAllProjects,name='projects'),
    path('<int:id>/',projectDetails,name='project-details'),
]