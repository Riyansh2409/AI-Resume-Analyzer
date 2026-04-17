from file_parser import extract_text

resume_path = input("Enter Resume file path: ")
job_text = input("Enter Job Description: ")

# Extract text from file
resume = extract_text(resume_path)

if resume is None:
    print("Unsupported file format!")
    exit()