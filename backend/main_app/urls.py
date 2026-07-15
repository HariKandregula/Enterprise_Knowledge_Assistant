from django.urls import path
from main_app import views

urlpatterns = [
    path("api/chat/", views.chat, name="chat"),
    path("api/documents/upload/", views.upload_document, name="upload_document")
]