from django.urls import path

from app.views import electron_lugat_detail, electron_lugat_view


urlpatterns = [
    path('list/', electron_lugat_view, name='list'),
    path('detail/<int:pk>', electron_lugat_detail, name='detail'),
]
