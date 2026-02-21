with open ("resume.txt", "r") as file:
    lines = file.read().split("\n")

bullet_points = ["•", "·", "⊛", "◉", "◉", "○", "◌", "-", "*"]

bullet_points_results = {}

for bullet_points_kind in bullet_points:
    bullet_points_count = lines.count(bullet_points_kind)
    bullet_points_results[bullet_points_kind] = bullet_points_count

total_bullet_points = sum(bullet_points_results.values())

bullet_lengths = []

for line in lines:
    line = line.strip()

    if line.startswith(bullet_points):
        clean_line = line[1:].strip()
        words = clean_line.split()
        word_count = len(words)
        bullet_lengths.append(word_count)

if len(bullet_lengths) > 0:
    average_lentgth = sum(bullet_lengths) / len(bullet_lengths)
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
    print("Buzzword score: Optimal number of bullet points")
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
