from django.urls import path
from music.views import (
    AlbumListView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView
)

app_name = 'music'

urlpatterns = [
    path('album/', AlbumListView.as_view(), name="album_list"),
    path('album/create', AlbumCreateView.as_view(), name="album_create"),
    path('album/<int:pk>/update', AlbumUpdateView.as_view(), name="album_update"),
    path('album/<int:pk/delete>', AlbumDeleteView.as_view(), name="album_delete"),
]