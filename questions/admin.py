from django.contrib import admin
from .models import Level, LevelWords, LevelQuestion

# Register your models here.
admin.site.register(Level)
admin.site.register(LevelWords)
admin.site.register(LevelQuestion)