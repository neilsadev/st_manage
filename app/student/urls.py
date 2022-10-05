from django.urls import path, include
from rest_framework.routers import DefaultRouter

from student import views

router = DefaultRouter()

urlpatterns = [
    path('', views.student_list),
    path('<uuid:id>', views.sstudent_detail_by_uid),
]
