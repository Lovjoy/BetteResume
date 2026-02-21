with open ("ray_resume.txt", "r") as file:
    words = file.read().split()

words_count = len(words)

print("Total words: ", words_count)

if words_count > 650:
    print("Too long, shorten your resume")
elif words_count >= 400:
    print("Good resume length!")
else:
    print("Too short, consider adding more to your resume")



