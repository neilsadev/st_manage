from django.urls import path, include
from rest_framework.routers import DefaultRouter

from institute import views

router = DefaultRouter()

urlpatterns = [
    path('', views.institute_list),
    path('<int:id>', views.institute_detail),
    path('<uuid:id>', views.institute_detail_by_uid)
]
