# CONSOLIDATED
with open ("ray_resume.txt", "r") as file:
    resume_text = file.read().lower()

structure = [
    "education", "experience", "skills", "projects", "certifications"
]

structure_results = {}

for structure_words in structure:
    structure_words_count = resume_text.count(structure_words)
    structure_results[structure_words] = structure_words_count

print("Structure Scan Results")
print("----------------------")

for structure_words, structure_words_count in structure_results.items():
    print(f"{structure_words}: {structure_words_count}")
    if structure_words_count >= 1:
        print("Great, you've included your", structure_words)
    else:
        print("You haven't included your ", structure_words)
