import re
import pymupdf

from django.shortcuts import render, get_object_or_404
from django.db.models import Avg, Max

from .models import ResumeAnalysis


def extract_text_from_pdf(pdf_file):
    text = ""

    document = pymupdf.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_name(text):
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if line and len(line) <= 60:
            return line

    return ""


def calculate_match_score(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    skills = [
        "python",
        "django",
        "django rest framework",
        "rest api",
        "api",
        "json",
        "mysql",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "git",
        "github",
        "crud",
        "orm",
        "django orm",
        "oop",
        "object oriented programming",
        "exception handling",
        "file handling",
        "authentication",
        "jwt",
        "bootstrap",
        "tailwind",
        "flask",
        "fastapi",
        "mongodb",
        "postgresql",
        "java",
        "c",
        "c++",
        "data structures",
        "problem solving",
    ]

    required_skills = []

    for skill in skills:
        if skill in job_description:
            required_skills.append(skill)

    if not required_skills:
        return 0, [], []

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    score = round(score, 2)

    return score, matched_skills, missing_skills


def home(request):

    analysis = None
    error = None
    job_description = ""

    if request.method == "POST":

        resume_file = request.FILES.get("resume")

        job_description = request.POST.get(
            "job_description",
            ""
        ).strip()

        if not resume_file:

            error = "Please upload a resume PDF."

        elif not resume_file.name.lower().endswith(".pdf"):

            error = "Only PDF files are allowed."

        elif not job_description:

            error = "Please enter the job description."

        else:

            try:

                resume_text = extract_text_from_pdf(
                    resume_file
                )

                if not resume_text.strip():

                    error = (
                        "Could not extract text from the PDF. "
                        "Please upload a text-based PDF."
                    )

                else:

                    name = extract_name(resume_text)

                    email = extract_email(resume_text)

                    phone = extract_phone(resume_text)

                    score, matched_skills, missing_skills = (
                        calculate_match_score(
                            resume_text,
                            job_description
                        )
                    )

                    analysis = ResumeAnalysis.objects.create(

                        name=name,

                        email=email,

                        phone=phone,

                        job_description=job_description,

                        match_score=score,

                        matched_skills=", ".join(
                            matched_skills
                        ),

                        missing_skills=", ".join(
                            missing_skills
                        ),

                        resume_text=resume_text,
                    )

            except Exception as e:

                error = f"Error analyzing resume: {str(e)}"

    # Dashboard statistics

    total_analyses = ResumeAnalysis.objects.count()

    average_score = ResumeAnalysis.objects.aggregate(
        Avg("match_score")
    )["match_score__avg"]

    highest_score = ResumeAnalysis.objects.aggregate(
        Max("match_score")
    )["match_score__max"]

    recent_analyses = ResumeAnalysis.objects.all().order_by(
        "-created_at"
    )[:5]

    if average_score is None:
        average_score = 0

    if highest_score is None:
        highest_score = 0

    context = {
        "analysis": analysis,
        "error": error,
        "job_description": job_description,

        "total_analyses": total_analyses,
        "average_score": round(average_score, 2),
        "highest_score": highest_score,

        "recent_analyses": recent_analyses,
    }

    return render(
        request,
        "analyzer/home.html",
        context
    )


def history(request):

    analyses = ResumeAnalysis.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "analyzer/history.html",
        {"analyses": analyses}
    )


def analysis_detail(request, pk):

    analysis = get_object_or_404(
        ResumeAnalysis,
        pk=pk
    )

    return render(
        request,
        "analyzer/analysis_detail.html",
        {"analysis": analysis}
    )


def delete_analysis(request, pk):

    analysis = get_object_or_404(
        ResumeAnalysis,
        pk=pk
    )

    if request.method == "POST":
        analysis.delete()

    analyses = ResumeAnalysis.objects.all().order_by(
        "-created_at"
    )

    return render(
        request,
        "analyzer/history.html",
        {"analyses": analyses}
    )