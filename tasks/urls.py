from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, test, create_task, show_task, update_task, delete_task


urlpatterns = [
    path('manager_dashboard/', manager_dashboard, name='manager_dashboard') ,
    path('user_dashboard/', user_dashboard) ,
    path('test/', test),
    path('create_task/', create_task, name='create_task'),
    path('show_task/', show_task),
    path('update_task/<int:id>/', update_task, name='update_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task')
]
