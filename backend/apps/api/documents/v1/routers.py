from django.urls import path
from . import views

app_name = "documents"

urlpatterns = [
    path("group-card/<int:pk>/", views.Document.as_view()),
    path("group-list/", views.GroupListDocument.as_view()),
]
