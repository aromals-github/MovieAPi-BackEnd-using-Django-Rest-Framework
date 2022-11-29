from django.contrib import admin
from .models import Movie,Rating


@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = ('title',)
    
@admin.register(Rating)
class Rating(admin.ModelAdmin):
    list_display = ('movie','user')