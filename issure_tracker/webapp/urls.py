from django.urls import path
from webapp.views import (
    IndexView,
    TracerView,
    CreateView,
    UpdateView,
    DeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('<int:pk>/', TracerView.as_view(), name='view'),
    path('add/', CreateView.as_view(), name='add'),
    path('<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),
    #
]