import os
import PyPDF2

RESUME_FOLDER = "data/resumes"
OUTPUT_FOLDER = "data/extracted_text"


# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def extract_text_from_pdf(pdf_path):

    text = ""

    try:
        with open(pdf_path, "rb") as file:

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted

    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

    return text


# Process all resumes
for filename in os.listdir(RESUME_FOLDER):

    if filename.endswith(".pdf"):

        pdf_path = os.path.join(RESUME_FOLDER, filename)

        print(f"Processing: {filename}")

        extracted_text = extract_text_from_pdf(pdf_path)

        # Save text file
        text_filename = filename.replace(".pdf", ".txt")

        text_path = os.path.join(OUTPUT_FOLDER, text_filename)

        with open(text_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)

print("\nAll resume texts extracted successfully!")