from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
	
    list_display = ["headline", "number", "filtre1", "filtre2", "publishing_date","slug"]
    search_fields = ["headline", "content"]
    list_editable = ["number", "filtre1", "filtre2"]	
    
    class Meta:
        model = Lesson

admin.site.register(Lesson, LessonAdmin)
