import re
import spacy

nlp = spacy.load("en_core_web_sm")

with open ("resume.txt", "r") as file:
    resume_text = file.read().lower()

doc = nlp(resume_text)

# ACTION VERB DETECTION ------------------------------------
action_verbs = []

for token in doc:
    if token.pos_ == "VERB":
        action_verbs.append(token.text)

# Count total verbs
total_action_verbs = len(action_verbs)

print("Action Verb Scan Results")
print("--------------------------")

for verb in action_verbs:
    print("Action verbs found: ", verb)

print("-----------------")
print(f"Total Action Verbs found: {total_action_verbs}")

if total_action_verbs >=15 :
    print("Buzzword score: Strong")
elif total_action_verbs>=8 :
    print("Buzzword score: Moderate")
else:
    print("Buzzword score: Weak")

situation_words = [
    "when", "while", "during", "at the time", 
    "faced", "encountered", "challenging", 
    "problem", "issue", "obstacle", "difficulty",
    "due to", "because", "under", "amidst", "in response to"
]
task_words = []
action_verbs =[]
result_words = []


# add a buffer since it catches extra word
# END OF ACTION VERB DETECTION --------------------------------------


# STAR DETECTION ----------------------------------------------------
for token in doc:
    if token.pos_ == "VERB":
        task_words.append(token.text)
    elif token.pos == "VERB":
        action_verbs.append(token.text)
    elif token.pos == "VERB":
        result_words.append(token.text)

sentences = re.split('[.!?]', resume_text)

star_score = 0

for sentence in sentences:
    sentence = sentence.strip()

    if len(sentence) == 0:
        continue

    has_s = any(word in sentence for word in situation_words)
    has_t = any(word in sentence for word in task_words)
    has_a = any(word in sentence for word in action_verbs)
    has_r = any(word in sentence for word in result_words)

    if has_s and has_t and has_a and has_r:
        star_score += 5
    elif has_s and has_t:
        star_score += 3
    elif has_t and has_a:
        star_score += 3
    elif has_a and has_r:
        star_score += 3
    elif has_s and has_r:
        star_score += 3
    elif has_s or has_t or has_a or has_r:
        star_score +=2
    else:
        print("Not enough STAR in your resume")

# END OF STAR DETECTION --------------------------------------------


# OVERUSED WORD DETECTION -------------------------------------------

action_verbs = []
action_verb_results = {}

for token in doc:
    if token.pos_ == "VERB":
        action_verbs.append(token.text)

for verb in action_verbs:
    count = resume_text.count(verb)
    action_verb_results[verb] = count

personality_words = [
    "hardworking", "dynamic", "motivated", "passionate", 
    "enthusiastic", "ambitious", "dedicated", "results-driven", 
    "detail-oriented", "proactive"
]
personality_results = {}

for word in personality_words:
    count = resume_text.count(word)
    personality_results[word] = count

fluff_words = [
    "strategic", "innovative", "cutting-edge", "best-in-class",
    "forward-thinking", "value-added", "game-changing", "world-class"
]
fluff_results = {}

for word in fluff_words:
    count = resume_text.count(word)
    fluff_results[word] = count

print("Overused Words Results")
print("----------------------")

for verb, count in action_verb_results.items():
    if count >= 3:
        print("⚠️ You've used the word \"", verb, "\" too many times")
    

for word, count in personality_results.items():
    if count >= 3:
        print("⚠️ You've used the word \"", verb, "\" too many times")

for word, count in fluff_results.items():
    if count >= 3:
        print("⚠️ You've used the word \"", verb, "\" too many times")


# END OF OVERUSED WORD DETECTION ---------------------------------------

# LENGTH CHECK ---------------------------------------------------------
with open ("resume.txt", "r") as file:
    words = file.read().split()

words_count = len(words)

print("Total words: ", words_count)

if words_count > 650:
    print("Too long, shorten your resume")
elif words_count >= 400:
    print("Good resume length!")
else:
    print("Too short, consider adding more to your resume")

# END OF LENGTH CHECK ---------------------------------------------------

# BULLET POINT CHECK ----------------------------------------------------

with open ("resume.txt", "r") as file:
    lines = file.read().split("\n")
    
bullet_points = ["•", "•", "·", "⊛", "◉", "◉", "○", "◌", "-", "*"]

bullet_points_results = {}
bullet_lengths = []

for line in lines:
    line = line.strip()

    if line.startswith(tuple(bullet_points)):

        bullet_symbol = line[0]
        bullet_points_results[bullet_symbol] = bullet_points_results.get(bullet_symbol, 0) + 1

        clean_line = line[1:].strip()
        word_count = len(clean_line.split())
        bullet_lengths.append(word_count)

total_bullet_points = sum(bullet_points_results.values())

if len(bullet_lengths) > 0:
    average_length = sum(bullet_lengths) / len(bullet_lengths)
else:
    average_length = 0


print("Bullet Point Scan Results")
print("---------------------------")

for bullet_points_kind, bullet_points_count in bullet_points_results.items():
    print(f"{bullet_points_kind}: {bullet_points_count}")

print("-----------------")
print(f"Total Bullet Points found: {total_bullet_points}")

if total_bullet_points >= 18:
    print("Too many bullet points, lessen them")
elif total_bullet_points>= 12:
    print("Optimal number of bullet points")
else:
    print("Not enough bullet points")

print("Calculating average length of bullet points")
print("--------------------------------------------")
print("Average words per bullet: ", round(average_length, 2))

if average_length >= 20:
    print("Length is too long, minimize them")
elif total_bullet_points>= 10:
    print("Optimal length of bullet point statements")
else:
    print("Too short, elaborate a little more!")

# END OF BULLET POINT CHECK -----------------------------------------



# STRUCTURE DETECTION CHECK -------------------------------------------

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

# END OF STRUCTURE DETECTION CHECK ---------------------------------------


# BUZZWORD SCANNER -------------------------------------------------------

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


# END OF BUZZWORD SCANNER



# QUANTIFICATION STRENGTH ANALYZER --------------------------------------

numbers = re.findall(r"\d+", resume_text)
score = 0

signals = {'$', '%', '+', '#', "minutes", "hours", "days", "weeks", "months", "years", 
           "increased", "reduced", "decreased", "improved", "grew", "boosted", "cut", "saved", "generated", "achieved", "delivered", "optimized",
           "expanded", "scaled", "accelerated", "percent", "clients", "customers", "users", "employees", "team", "teams", "projects", "revenus",
           "sales", "profit", "budget", "cost", "time"}

for signals_kinds in signals:
    if signals_kinds or numbers in resume_text:
        score += 2

print("Quantification Strength Results:")
print("---------------------------------")

if score >= 30:
    print("Good job on quantifying! Your score is ", score)
elif score >= 20:
    print("Consider quantifying your impact/results more. Your score is ", score)
else:
    print("Quantification strengths weak! Your score is ", score)


# END OF QUANTIFICATION STRENGTH ANALYZER ----------------------------------------------



