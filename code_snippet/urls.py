from django.urls import path
from code_snippet import views

urlpatterns = [
    path("snippets/", views.code_snippet_list),
    path("snippets/<int:pk>/", views.code_snippet_detail),
]
