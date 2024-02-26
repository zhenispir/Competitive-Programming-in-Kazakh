a = input().lower()
for i in a:
    if i not in "aeiouy":
        print("." + i, end="")