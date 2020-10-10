from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
# http http://127.0.0.1:8000/snippets -->
# --->suffix :
# from rest_framework.urlpatterns import format_suffix_patterns
# --> http http://127.0.0.1:8000/snippets.json  # JSON suffix
# --> http http: //127.0.0.1: 8000/snippets.api   # Browsable API suffix
urlpatterns = format_suffix_patterns(urlpatterns)
# -->Content-Type :
'''
    # POST using form data
    http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"

    # POST using JSON
    http --json POST http://127.0.0.1:8000/snippets/ code="print(456)"
'''
