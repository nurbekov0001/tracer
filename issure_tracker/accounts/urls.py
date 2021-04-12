from django.urls import path
from accounts.views import logout_view, login_view, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', RegisterView.as_view(), name='create')
]