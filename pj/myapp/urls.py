from django.urls import path,include
from .views import *

urlpatterns = [
    path("",course_list,name="list" ),
    # path("", include(myapp.urls)),
]
