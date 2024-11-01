from django.contrib import admin
from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["question_text"]
    list_filter = ['pub_date']  # Consider filtering by date instead
    list_display = ["question_text", "pub_date", "was_published_recently"]
    ordering = ['question_text']  # This orders the questions alphabeticallyi
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

