from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
#usbaiの中のurls.pyをルーティングに組み込む
    path("usbai/",include("usbai.urls")),
]
