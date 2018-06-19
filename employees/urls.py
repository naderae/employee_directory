from . import views
from django.urls import path
from . import views
# from django.conf.urls import url

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create'),
    # path('create/', views.create, name='create'),
    # path('delete/<int:course_id>/', views.delete, name='delete'),

]
