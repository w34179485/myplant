from django.urls import path
from . import views

app_name = 'merchandise'

urlpatterns = [
    path('',views.merchandise_list,name='index'),
    path('add/',views.merchandise_add,name='add'),
    path('<int:p_id>/remove/',views.merchandise_remove,name='remove'),
    path('<int:p_id>/update/',views.merchandise_update,name='update'),
]