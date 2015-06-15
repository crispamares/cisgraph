from django.contrib import admin

# Register your models here.
from .models import Poll, Question, Choice, Facet, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)  # Choices inline
admin.site.register(Facet)
admin.site.register(Answer)
