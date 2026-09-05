sample_list = []

with open("sample.txt", "r") as f:
    for text in f:
        sample_list.append(text.strip())

print(sample_list)

