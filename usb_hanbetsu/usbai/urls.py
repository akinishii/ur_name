from django.urls import path
from . import views

app_name="usbai"
urlpatterns=[
    path("",views.index,name="index"),
    path("predict/",views.predict,name="predict"),
]