from django.urls import path
from .views import getAllProjects, projectDetails,getTopProjects

app_name = 'projects'
urlpatterns = [
    path('',getAllProjects,name='projects'),
    path('top/',getTopProjects, name='top-projects'),
    path('<int:id>/',projectDetails,name='project-details'),
]