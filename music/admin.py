from django.contrib import admin
from .models import Album, Track
# Register your models here.

class TrackInline(admin.TabularInline):
    model = Track


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (TrackInline, )
