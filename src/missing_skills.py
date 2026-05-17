import os
from skills import SKILLS


# Resume folder
RESUME_FOLDER = "data/cleaned_resumes"

# Job description file
JOB_DESCRIPTION_FILE = "data/job_descriptions/it_support.txt"


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# Read job description
with open(JOB_DESCRIPTION_FILE, "r", encoding="utf-8") as file:

    job_description = file.read().lower()

required_skills = extract_skills(job_description)

print("\n" + "=" * 60)
print("REQUIRED JOB SKILLS")
print("=" * 60)

print(required_skills)


# Process resumes
for filename in os.listdir(RESUME_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(RESUME_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            resume_text = file.read().lower()

        candidate_skills = extract_skills(resume_text)

        missing_skills = list(
            set(required_skills) - set(candidate_skills)
        )

        matched_skills = list(
            set(required_skills) & set(candidate_skills)
        )

        print("\n" + "=" * 60)
        print(f"Resume: {filename}")
        print("=" * 60)

        print(f"Matched Skills: {matched_skills}")
        print(f"Missing Skills: {missing_skills}")