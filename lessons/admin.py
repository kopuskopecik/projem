from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
	
    list_display = ["headline","number", ]	
    search_fields = ["headline", "content"]
    list_editable = ["number"]	
    
    class Meta:
        model = Lesson

admin.site.register(Lesson, LessonAdmin)
