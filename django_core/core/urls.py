from django.contrib import admin
from django.urls import path, include

from core.api.views import ListViewStuffs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', ListViewStuffs.as_view()),
]
