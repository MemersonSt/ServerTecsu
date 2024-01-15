from django.urls import path
from .views import Login, Logout, UserCreate, UserList, UserUpdate, EstudentCreate, EstudentUpdate, EstudentDelete, EstudentList, VincularEstudiante, EstudentDetail, UserDetail

urlpatterns = [
    # USUARIOS/PADRES DE FAMILIA
    path('user/', Login.as_view(), name = 'login'),
    path('user/logout/', Logout.as_view(), name = 'logout'),
    path('user/create/', UserCreate.as_view(), name = 'user_create'),
    path('user/search/', UserDetail.as_view(), name = 'user_search'),
    path('user/update/<int:pk>/', UserUpdate.as_view(), name = 'user_update'),
    path('user/list/', UserList.as_view(), name = 'user_list'),
    # ESTUDIANTES
    path('estudent/create/', EstudentCreate.as_view(), name = 'estudent_create'),
    path('estudent/update/', EstudentUpdate.as_view(), name = 'estudent_update'),
    path('estudent/search/', EstudentDetail.as_view(), name = 'estudent_search'),
    path('estudent/update/<int:pk>/', EstudentUpdate.as_view(), name = 'estudent_update'),
    path('estudent/delete/<int:pk>/', EstudentDelete.as_view(), name = 'estudent_delete'),
    path('estudent/list/', EstudentList.as_view(), name = 'estudent_list'),
    path('estudent/vincular/', VincularEstudiante.as_view(), name = 'vincular_estudiante'),
]
