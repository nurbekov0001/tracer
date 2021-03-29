from django.urls import path
from webapp.views import (
    IndexView,
    TracerView,
    UpdateView,
    DeleteView,
    ProjectTracerCreate,
    ProjectCreateView,
    ProjectIndexView,
    ProjectView,
    ProjectDeleteView,
    ProjectUpdateView
)

urlpatterns = [
    path('tracers/', IndexView.as_view(), name='list'),
    path('<int:pk>/', TracerView.as_view(), name='view'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),

    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project_tracer/<int:pk>/add/', ProjectTracerCreate.as_view(), name='project_tracer_add'),
    path('', ProjectIndexView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

]
