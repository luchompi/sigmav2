from django.urls import path as p
from . import views as v
from rest_framework.urlpatterns import format_suffix_patterns
app_name="empresa"

urlpatterns=[
#API urls
p('sedes/',v.SedeAPI.as_view()),
p('sedes/<int:pk>',v.SedeAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)