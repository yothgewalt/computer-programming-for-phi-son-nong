scores = [85, 90, 78, 92, 88]
print("Scores:", scores)

print("Highest score:", max(scores))
print("Lowest score:", min(scores))

"""
Find the sum of scores and total of members of scores
sum / member_length
"""

sum_of_scores = sum(scores)
total_members_of_scores = len(scores)
average_of_scores = sum_of_scores / total_members_of_scores
print("Average score:", average_of_scores)

count = 0
for x in scores:
    if x > 85:
        count += 1
print("Scores above:", count)

scores.sort(reverse=True)
print("Sorted scores:", scores)
