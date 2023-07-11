from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('create/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('change-password/', views.UserChangePasswordView.as_view(), name='change_password'),
]
