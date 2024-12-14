from django.urls import path
from .views import index, menu, signin, signup, signout, tasks


urlpatterns = [
    path('', index, name='home'),
    path('menu/', menu, name='menu'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
    path('tasks/', tasks, name='tasks'),
]