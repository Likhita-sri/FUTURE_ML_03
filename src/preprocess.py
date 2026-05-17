import os
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Input and output folders
INPUT_FOLDER = "data/extracted_text"
OUTPUT_FOLDER = "data/cleaned_resumes"

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_resume(text):

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatization
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words back
    cleaned_text = " ".join(words)

    return cleaned_text


# Process all extracted text files
for filename in os.listdir(INPUT_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(INPUT_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            raw_text = file.read()

        cleaned_text = clean_resume(raw_text)

        # Save cleaned resume
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)

        print(f"Cleaned: {filename}")

print("\nAll resumes cleaned successfully!")