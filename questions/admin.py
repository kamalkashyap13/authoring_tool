from django.contrib import admin
from .models import Level, LevelWords, LevelQuestion, OffWords

# Register your models here.
admin.site.register(Level)
admin.site.register(LevelWords)
admin.site.register(OffWords)
admin.site.register(LevelQuestion)