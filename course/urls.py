from django.urls import path
from .views import course_list, add_course, update_course, delete_course

urlpatterns = [
    path('', course_list, name='course_list'),
    path('add/', add_course, name='add_course'),
    path('course/update/<int:course_id>/',update_course,name='update_course'),
    path('course/delete/<int:course_id>/',delete_course, name='delete_course'),
]
