from django.db import models


class ResumeAnalysis(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)

    job_description = models.TextField()

    match_score = models.FloatField(default=0)

    matched_skills = models.TextField(blank=True)
    missing_skills = models.TextField(blank=True)

    resume_text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.match_score}%"