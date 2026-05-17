import os
import json
from skills import SKILLS

CLEANED_FOLDER = "data/cleaned_resumes"
OUTPUT_FOLDER = "data/extracted_skills"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# Process resumes
for filename in os.listdir(CLEANED_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(CLEANED_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            resume_text = file.read()
            print("\n")
            print(filename)
            print(resume_text[:1000])

        skills_found = extract_skills(resume_text)

        # Save skills JSON
        output_file = filename.replace(".txt", ".json")

        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        with open(output_path, "w") as json_file:
            json.dump(skills_found, json_file, indent=4)

        print(f"Skills extracted from: {filename}")

print("\nSkill extraction completed successfully!")