from django.urls import path
from accounts.views import logout_view, login_view, register_view, UserDetailView, UserView,\
    UserChangeView, UserPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('users/', UserView.as_view(), name='user'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change')

]