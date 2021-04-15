from django.urls import path
from webapp.views import (
    IndexView,
    TracerView,
    TracerDeleteView,
    TracerUpdateView,
    ProjectTracerCreate,
    ProjectCreateView,
    ProjectIndexView,
    ProjectView,
    ProjectDeleteView,
    ProjectUpdateView,
    UserUpdateView
)

app_name = 'project'

urlpatterns = [
    path('tracers/', IndexView.as_view(), name='list'),
    path('<int:pk>/', TracerView.as_view(), name='view'),
    path('<int:pk>/update/', TracerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TracerDeleteView.as_view(), name='delete'),

    path('user/<int:pk>', UserUpdateView.as_view(), name="user_update"),

    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project_tracer/<int:pk>/add/', ProjectTracerCreate.as_view(), name='project_tracer_add'),
    path('', ProjectIndexView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

]
