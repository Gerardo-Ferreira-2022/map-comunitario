from django.urls import path
from .views import index, menu, signin, signup, signout, tasks, usuarios
from . import views


urlpatterns = [
    path('', index, name='home'),
    path('menu/', menu, name='menu'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('tasks/', tasks, name='tasks'),
    path('usuarios/', usuarios, name='usuarios'),
    path('eliminar_usuario/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('actualizar_usuario/<int:user_id>/', views.actualizar_usuario, name='actualizar_usuario'),
]