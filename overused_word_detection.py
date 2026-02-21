# idea for this is that this scans for a specific thing, (eg: action verbs, skills, job description) and tells you if you overused it
import spacy

nlp = spacy.load("en_core_web_sm")

with open ("resume.txt", "r") as file:
    resume_text = file.read()

doc = nlp(resume_text)

action_verbs = {}
personality_words = { 
    "hardworking", "dynamic", "motivated", "passionate", 
    "enthusiastic", "ambitious", "dedicated", "results-driven", 
    "detail-oriented", "proactive"
}
fluff_words = {
    "strategic", "innovative", "cutting-edge", "best-in-class",
    "forward-thinking", "value-added", "game-changing", "world-class"
    }

for token in doc:
    if token.pos_ == "VERB":
        action_verbs.append(token.text)


for action_verbs_words in action_verbs:
    action_verbs_count = resume_text.count(action_verbs_words)
    action_verb_results = [action_verbs_words] = action_verbs_count

for personality in personality_words:
    personality_words_count = resume_text.count(personality)
    personality_results = [personality] = personality_words_count

for fluff in fluff_words:
    fluff_words_count = resume_text.count(fluff)
    fluff_results = [fluff] = fluff_words_count

print("Overused Words Results")
print("----------------------")

for action_verbs_words, action_verbs_count in action_verb_results.items():
    print(f"{action_verbs_words}: {action_verbs_count}")
    if action_verbs_count >= 3:
        print("You've used the word ", action_verbs_words, " too many times")

for personality, personality_words_count in personality_results.items():
    print(f"{personality}: {personality_words_count}")
    if personality_words_count >= 3:
        print("You've used the word ", personality, " too many times")

for fluff, fluff_words_count in fluff_results.items():
    print(f"{fluff}: {fluff_words_count}")
    if fluff_words_count >= 3:
        print("You've used the word ", fluff, " too many times")

