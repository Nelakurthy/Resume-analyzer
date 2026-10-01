from django.contrib import admin
from .models import ResumeAnalysis


@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "match_score",
        "created_at",
    )

    list_filter = ("created_at",)

    search_fields = (
        "name",
        "email",
    )