import spacy

nlp = spacy.load("en_core_web_sm")

with open ("ray_resume.txt", "r") as file:
    resume_text = file.read().lower()

doc = nlp(resume_text)

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

# add a buffer since it catches extra word

