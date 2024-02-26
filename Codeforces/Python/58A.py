def check_hello(word):
    hello = "hello"
    hello_index = 0

    for char in word:
        if char == hello[hello_index]:
            hello_index += 1
            if hello_index == len(hello):
                return "YES"

    return "NO"

# Example usage
word = input()
result = check_hello(word)
print(result)