# CONSOLIDATED
# # this one is still unfinished

import re
import spacy

nlp = spacy.load("en_core_web_sm")

situation_words = [
    "when", "while", "during", "at the time", 
    "faced", "encountered", "challenging", 
    "problem", "issue", "obstacle", "difficulty",
    "due to", "because", "under", "amidst", "in response to"
]
task_words = []
action_verbs =[]
result_words = []

with open ("ray_resume.txt", "r") as file:
    resume_text = file.read().lower()

doc = nlp(resume_text)

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


