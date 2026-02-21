# CONSOLIDATED
# idea for this is that this scans for a specific thing, (eg: action verbs, skills, job description) and tells you if you overused it
import spacy

nlp = spacy.load("en_core_web_sm")

with open ("ray_resume.txt", "r") as file:
    resume_text = file.read()

doc = nlp(resume_text)

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