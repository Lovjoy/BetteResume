with open ("ray_resume.txt", "r") as file:
    resume_text = file.read().lower()

skills = [
    "Artificial Intelligence", "Python",
    "Artificial Intelligence", "Java",
    "Django",
    "Keras",
    "Software Engineering",
    "Keras", "Machine Learning",
    "Machine Learning", "Data Science",
    "Artificial Intelligence", "Data Analysis", "Machine Learning",
    "Artificial Intelligence", "Machine Learning", "Python",
    "Java", "Machine Learning", "Python",
    "Data Structures",
    "Django", "Machine Learning",
    "Data Structures", "Machine Learning",
    "Data Analysis", "Data Science",
    "Python", "Data Science",
    "Machine Learning", "Software Engineering",
    "Java", "SQL",
    "Data Analysis", "Machine Learning", "Data Science",
    "Machine Learning", "Python", "Data Science", 
    "Artificial Intelligence", "Java", "Machine Learning"
]

job_skills= [
    "Databases",
    "ML Applications",
    "Async Functions",
    "Large-Scale Models",
    "Data Pipeline",
    "Data Visualization",
    "Data Analysis",
    "Data Cleaning",
    "Windows",
    "C++",
    "Databases", "ML Applications",
    "Databases", "Async Functions",
    "ML Applications", "Async Functions",
    "Large-Scale Models", "Data Pipeline",
    "Data Visualization", "Large-Scale Models",
    "Data Analysis", "Large-Scale Models",
    "Data Cleaning", "Large-Scale Models",
    "Data Visualization", "Data Pipeline",
    "Data Analysis", "Data Pipeline",
    "Data Cleaning", "Data Pipeline"
]

responsibilities = [
    "Deployment", "Training",
    "Mentorship", "Industry",
    "Monitoring", "Software",
    "Support", "Troubleshooting", "Collaboration", "Documentation", "System",
    "Technical",
    "Trends", "Field",
    "Visits",
    "Collaboration",
    "Collaboration", "Model",
    "Deployment", "Documentation", "Analytical",
    "Integration", "Innovation", "Cross-Functional",
    "Skills", "Communication", "Team",
    "Training", "AI",
    "Velocity", "Infrastructure"
]

majors = [
    "Instrumentation and Control",
    "Hons. Mechanical Engineering",
    "Industrial Education",
    "Advertising & Public Relations",
    "Computer Engineering",
    "Electronics Engineering Technology",
    "Computer Science and Management",
    "Advanced Analytics",
    "Electronics and Communication",
    "Data Science and Engineering",
    "Engineering Management",
    "Chemical Engineering",
    "Computer Science",
    "Cybersecurity",
    "Telecommunication",
    "Management Information System",
    "Electrical Engineering Technology",
    "General Studies",
    "International Business"
]

previous_positions = [
    "Software Developer (Machine Learning Engineer)",
    "Business Analyst",
    "Statistical Analyst",
    "Analyst Support",
    "Data Strategy and Delivery Specialist",
    "Web Developer Intern",
    "Machine Learning Engineer Intern",
    "NLP Analyst",
    "Teaching Assistant",
    "Junior Data Engineer",
    "Analyst Intern",
    "Product Engineer Intern",
    "BI Engineer",
    "Junior Machine Learning Engineer",
    "Associate Researcher",
    "Associate Analyst",
    "Software Developer ML",
    "Data Scientist - Analytics & Insights",
    "Jr. Data Scientist",
    "Associate System Engineer Intern"
]

buzzwords = skills + job_skills + responsibilities + majors + previous_positions

buzzwords = [word.lower() for word in buzzwords]

buzzwords_results = {}

for buzzword_word in buzzwords:
    buzzwords_count = resume_text.count(buzzword_word)
    buzzwords_results[buzzword_word] = buzzwords_count

total_buzzwords = sum(buzzwords_results.values())

print("Buzzword Scan Results")
print("----------------------")

'''
for buzzword_word, buzzwords_count in buzzwords_results.items():
    print(f"{buzzword_word}: {buzzwords_count}")
'''

print("-----------------")
print(f"Total Buzzwords found: {total_buzzwords}")

if total_buzzwords >= 5:
    print("Buzzword score: Strong")
elif total_buzzwords>= 3:
    print("Buzzword score: Moderate")
else:
    print("Buzzword score: Weak")


