from django.contrib import admin
from django.urls import path, include
from task_manager import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('login/', views.SignIn.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('admin/', admin.site.urls),
]
