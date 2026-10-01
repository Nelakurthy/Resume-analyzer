import re


SKILLS = [
    "python",
    "django",
    "fastapi",
    "flask",
    "rest api",
    "mysql",
    "mongodb",
    "sql",
    "html",
    "html5",
    "css",
    "css3",
    "javascript",
    "typescript",
    "react",
    "react.js",
    "tailwind css",
    "node.js",
    "git",
    "github",
    "docker",
    "linux",
    "java",
    "c",
    "c++",
    "data structures",
    "algorithms",
    "dsa",
    "machine learning",
    "artificial intelligence",
]


def normalize_text(text):
    """
    Convert text into a consistent format
    for skill matching.
    """

    text = text.lower()

    # Convert REST APIs to REST API
    text = re.sub(r"\brest\s+apis\b", "rest api", text)

    # Convert multiple spaces into one space
    text = re.sub(r"\s+", " ", text)

    return text


def extract_skills(text):

    text = normalize_text(text)

    found_skills = []

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(
            skill.lower()
        ) + r"(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return list(dict.fromkeys(found_skills))


def analyze_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matched_skills = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    if job_skills:

        match_percentage = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )

    else:

        match_percentage = 0

    return {
        "match_percentage": match_percentage,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }