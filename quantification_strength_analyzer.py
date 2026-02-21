import re

with open ("resume.txt", "r") as file:
    resume_text = file.read()

numbers = re.findall(r"\d+", resume_text)

signals = {'$', '%', '+', '#', (any(char.isdigit() for char in resume_text)), "minutes", "hours", "days", "weeks", "months", "years", numbers, 
           "increased", "reduced", "decreased", "improved", "grew", "boosted", "cut", "saved", "generated", "achieved", "delivered", "optimized",
           "expanded", "scaled", "accelerated", "percent", "clients", "customers", "users", "employees", "team", "teams", "projects", "revenus",
           "sales", "profit", "budget", "cost", "time"}

for signals_kinds in signals:
    if signals_kinds in resume_text:
        score += 2

print("Quantification Strength Results:")
print("---------------------------------")

if score >= 30:
    print("Good job on quantifying! Your score is ", score)
elif score >= 20:
    print("Consider quantifying your impact/results more. Your score is ", score)
else:
    print("Quantification strengths weak! Your score is ", score)