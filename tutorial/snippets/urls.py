from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import *

urlpatterns = [
   path('snippets/', SnippetList.as_view()),
   path('snippets/<int:pk>/', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)