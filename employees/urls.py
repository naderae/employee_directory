from . import views
from django.urls import path
from . import views
# from django.conf.urls import url

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),
    # path('create/', views.create, name='create'),
    # path('delete/<int:course_id>/', views.delete, name='delete'),

]
