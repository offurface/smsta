from django.urls import path
from . import views

app_name = "system"

urlpatterns = [
    path("groups/", views.AcademicGroupList.as_view()),
    path("groups/<int:pk>/", views.AcademicGroupDetail.as_view()),
]
