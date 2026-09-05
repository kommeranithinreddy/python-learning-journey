from collections import Counter

marks = [85, 90, 85, 72, 90, 85, 60, 72, 90, 95, 85]

marks_count = Counter(marks)
print(marks_count)
print(marks_count[85])
print(marks_count.most_common(3))
